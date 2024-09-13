"""Metadata module."""

__docformat__ = "numpy"
import json
from dataclasses import dataclass
from dataclasses import field as dc_field
from typing import Any, Dict, List, NamedTuple, Optional, Set, Union
from urllib.parse import ParseResult as UrlParseResult
from urllib.parse import SplitResult as UrlSplitResult
from urllib.parse import urlparse, urlsplit, urlunparse, urlunsplit

import pandas as pd

import smlc.type as T

ParsedURL = Union[UrlParseResult, UrlSplitResult]
"""See `MetadataManager` constructor."""


class MetadataManager:
    """Metadata manager."""

    def __init__(
        self,
        spliturl: bool = False,
    ):
        """
        Parameters
        ----------
        spliturl : bool, default `False`
            `False` for [RFC 1808](https://datatracker.ietf.org/doc/html/rfc1808.html),
            `True` for [RFC 2396](https://datatracker.ietf.org/doc/html/rfc2396.html).
            See [urllib doc](https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse).
        """

        self._tables: Set[NamedTuple] = set()
        if spliturl:
            self._s2t = urlsplit
            self._t2s = urlunsplit
        else:
            self._s2t = urlparse
            self._t2s = urlunparse

    def table_is_registered(
        self,
        turl: Union[str, ParsedURL],
    ) -> bool:
        """
        Parameters
        ----------
        turl : Union[str, `ParsedURL`]
            Table's URL.

        Examples
        --------
        >>> import pathlib
        >>> from tempfile import NamedTemporaryFile
        >>> t1fp = NamedTemporaryFile("w")
        >>> t1_url = pathlib.Path(t1fp.name).absolute().as_uri()
        >>> mm = MetadataManager()
        >>> mm.table_is_registered(t1_url)
        False
        >>> mm.register_table(t1_url)
        ParseResult(scheme='file', netloc='', path=..., params='', query='', fragment='')
        >>> mm.table_is_registered(t1_url)
        True
        >>> mm.unregister_table(t1_url)
        >>> mm.table_is_registered(t1_url)
        False
        """

        if not isinstance(turl, ParsedURL):
            turl = self._s2t(turl)
        return turl in self._tables

    def register_table(
        self,
        turl: Union[str, ParsedURL],
        raise_registered: bool = True,
    ) -> ParsedURL:
        """
        Parameters
        ----------
        turl : Union[str, `ParsedURL`]
            Table's URL.
        raise_registered : bool, default `True`
            If `True`, raises `ValueError` when caller tries to register already registered table.

        Examples
        --------
        >>> import pathlib
        >>> from tempfile import NamedTemporaryFile
        >>> t1fp = NamedTemporaryFile("w")
        >>> t1_url = pathlib.Path(t1fp.name).absolute().as_uri()
        >>> mm = MetadataManager()
        >>> mm.register_table(t1_url)
        ParseResult(scheme='file', netloc='', path=..., params='', query='', fragment='')
        >>> mm.register_table(t1_url)
        Traceback (most recent call last):
            ...
        ValueError: table ... is already registered
        >>> t2fp = NamedTemporaryFile("w")
        >>> t2_url = pathlib.Path(t2fp.name).absolute().as_uri()
        >>> mm.register_table(t2_url)
        ParseResult(scheme='file', netloc='', path=..., params='', query='', fragment='')
        """

        if not isinstance(turl, ParsedURL):
            turl = self._s2t(turl)
        if turl in self._tables:
            if raise_registered:
                raise ValueError(f"table {self._t2s(turl)} is already registered")
        else:
            self._tables.add(turl)
        return turl

    def unregister_table(
        self,
        turl: Union[str, ParsedURL],
    ):
        """
        Parameters
        ----------
        turl : Union[str, `ParsedURL`]
            Table's URL.

        Examples
        --------
        >>> import pathlib
        >>> from tempfile import NamedTemporaryFile
        >>> t1fp = NamedTemporaryFile("w")
        >>> t1_url = pathlib.Path(t1fp.name).absolute().as_uri()
        >>> mm = MetadataManager()
        >>> mm.register_table(t1_url)
        ParseResult(scheme='file', netloc='', path=..., params='', query='', fragment='')
        >>> mm.register_table(t1_url)
        Traceback (most recent call last):
            ...
        ValueError: table ... is already registered
        >>> mm.unregister_table(t1_url)
        >>> mm.register_table(t1_url)
        ParseResult(scheme='file', netloc='', path=..., params='', query='', fragment='')
        >>> mm.unregister_table(t1_url)
        >>> mm.unregister_table(t1_url)
        Traceback (most recent call last):
            ...
        KeyError: 'table ... is not registered'
        """

        if not isinstance(turl, ParsedURL):
            turl = self._s2t(turl)
        if turl in self._tables:
            self._tables.remove(turl)
        else:
            raise KeyError(f"table {self._t2s(turl)} is not registered")

    def knowledge_base_for_table(
        self,
        turl: Union[str, ParsedURL],
        **kwargs,
    ) -> "KnowledgeBaseForTable":
        """Convenient factory for `KnowledgeBaseForTable`.
        `mm.knowledge_base_for_table(turl, **kwargs)` is equivalent of
        `KnowledgeBaseForTable(mm, turl, **kwargs)`. If table is not registered,
        registers table.

        Parameters
        ----------
        turl : Union[str, `ParsedURL`]
            Table's URL.
        **kwargs :
            Named arguments passed to `KnowledgeBaseForTable` constructor.

        Examples
        --------
        >>> import pathlib
        >>> from tempfile import NamedTemporaryFile
        >>> t1fp = NamedTemporaryFile("w")
        >>> t1_url = pathlib.Path(t1fp.name).absolute().as_uri()
        >>> mm = MetadataManager()
        >>> kb = mm.knowledge_base_for_table(t1_url)
        """
        return KnowledgeBaseForTable(self, turl)


class KnowledgeBaseForTable:
    """Knowledge base for single table.

    Attributes are computed on-demand (lazy evaluation) and then stored. If you want to
    recompute an attribute, delete (`del knowledge_base.attr`) and re-evaluate it.
    """

    def __init__(
        self,
        mm: MetadataManager,
        turl: Union[str, ParsedURL],
        unregister_table_on_deletion: bool = False,
    ):
        """Calling `MetadataManager`.`knowledge_base_for_table` factory is preferable.

        Parameters
        ----------
        mm : `MetadataManager`
        turl : `Union[str, ParsedUrl]`
            Table's URL.
        unregister_table_on_deletion: bool, defaults `False`
            If `True`, `del knowledge_base` unregisteres table.

        Examples
        --------
        >>> import pathlib
        >>> from tempfile import NamedTemporaryFile
        >>> t1fp = NamedTemporaryFile("w")
        >>> t1_url = pathlib.Path(t1fp.name).absolute().as_uri()
        >>> mm = MetadataManager()
        >>> kb = KnowledgeBaseForTable(mm, t1_url)
        >>> del kb
        >>> mm.table_is_registered(t1_url)
        True
        >>> kb = KnowledgeBaseForTable(mm, t1_url, unregister_table_on_deletion = True)
        >>> del kb
        >>> mm.table_is_registered(t1_url)
        False
        """
        self._mm = mm
        self._turl = mm.register_table(turl, raise_registered=False)
        self._unregister_table_on_deletion = unregister_table_on_deletion
        self._storage: Dict[str, Any] = dict()
        # valid keys for _storage
        self._slots = [
            "n_rows",
        ]

    def __del__(self):
        if self._unregister_table_on_deletion:
            self._mm.unregister_table(self.turl)

    @property
    def turl(self) -> ParsedURL:
        """Table URL (parsed)."""
        return self._turl


#     @property
#     def n_rows(self) -> int:
#         if "n_rows" not in self._storage:
#             self._storage["n_rows"] = self._table.shape[0]
#         return self._storage["n_rows"]

#     @n_rows.deleter
#     def n_rows(self) -> None:
#         if "n_rows" in self._storage:
#             del self._storage["n_rows"]

#     # TODO
#     def column_metadata(self, col: Union[str, list[str]]):
#         pass


@dataclass(frozen=True)
class ColumnType:
    physical: T.PhysicalType
    logical: T.LogicalType
    # this might stop being optional
    # once implementation of SemanticType is established
    semantic: Optional[T.SemanticType] = None
    # Value constraints are supposed to be immutable.
    # For this reason we don't use dataclasses.field(default_factory=T.AnyValue).
    value_constraint: T.ValueConstraint = T.AnyValue()


# # TODO
# class ColumnMetadata:
#     """Column metadata. Column type, description, origin and descriptive statistics."""

#     def __init__(
#         self,
#         table_id: int,
#         column_name: str,
#         column_type: ColumnType,
#         description: str = "<missing>",
#         origin: str = "<unknown>",
#     ):
#         self._table_id = table_id
#         self._column_name = column_name
#         self._column_type = column_type
#         self._description = description
#         self._origin = origin
#         self._storage = ColumnMetadataStorage(table_id, column_name)
#         # valid keys for _storage
#         self._slots = ["descriptive_stats"]

#     @property
#     def table_id(self) -> int:
#         return self._table_id

#     @property
#     def column_name(self) -> str:
#         return self._column_name

#     @property
#     def column_type(self) -> ColumnType:
#         return self._column_type

#     @property
#     def description(self) -> str:
#         return self._description

#     @property
#     def origin(self) -> str:
#         return self._origin


# class ColumnMetadataStorage:
#     """Dict-like. Allows to get, set and delete multiple entries at once."""

#     def __init__(self, table_id: int, column_name: str):
#         self._table_id = table_id
#         self._column_name = column_name
#         self._dict: Dict[str, ColumnMetadata] = dict()

#     @property
#     def table_id(self) -> int:
#         return self._table_id

#     @property
#     def column_name(self) -> str:
#         return self._column_name

#     def __getitem__(
#         self, col: Union[str, List[str]]
#     ) -> Union[ColumnMetadata, List[ColumnMetadata]]:
#         if isinstance(col, str):
#             return self._dict[col]
#         else:
#             res = list()
#             for c in col:
#                 res.append(self._dict[c])
#             return res

#     def __delitem__(self, col: Union[str, List[str]]) -> None:
#         if isinstance(col, str):
#             del self._dict[col]
#         else:
#             for c in col:
#                 del self._dict[c]

#     def __setitem__(
#         self,
#         col: Union[str, List[str]],
#         val: Union[ColumnMetadata, List[ColumnMetadata]],
#     ) -> None:
#         # TODO typecheck val?
#         if isinstance(col, str):
#             # TODO typecheck val?
#             self._dict[col] = val
#         else:
#             # TODO typecheck val?
#             for c, v in col:
#                 self._dict[c] = v


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.ELLIPSIS)
