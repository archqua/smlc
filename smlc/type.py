"""
Typing utilities that can help to define what a column type is.
"""

__docformat__ = "numpy"
from abc import ABC, abstractmethod
from enum import StrEnum, ReprEnum, auto
from typing import Any, Type, Union


class PhysicalType(StrEnum):
    """
    Physical type.
    64-, 32-, 16- and 8-bit signed and unsigned integers and floats; ASCII- and UTF8-strings.

    """

    i64 = auto()
    """Signed 64-bit integer."""
    i32 = auto()
    """Signed 32-bit integer."""
    i16 = auto()
    """Signed 16-bit integer."""
    i8 = auto()
    """Signed 8-bit integer."""
    u64 = auto()
    """Unsigned 64-bit integer."""
    u32 = auto()
    """Unsigned 32-bit integer."""
    u16 = auto()
    """Unsigned 16-bit integer."""
    u8 = auto()
    """Unsigned 8-bit integer."""
    f64 = auto()
    """64-bit floating point number."""
    f32 = auto()
    """32-bit floating point number."""
    f16 = auto()
    """16-bit floating point number."""
    f8 = auto()
    """8-bit floating point number."""
    ascii_str = auto()
    """ASCII-string."""
    utf8_str = auto()
    """UTF8-string."""


class LogicalType(StrEnum):
    """
    Logical type.
    Natural number, integer, real number, text, boolean, enum, time and timedelta.
    """

    boolean = auto()
    """True or false (exclusive). Allows negation, conjunction and disjunction."""
    enum = auto()
    """Several possible values. No arithmetic. No order."""
    natural = auto()
    """Non-negative integers."""
    integer = auto()
    """Integers."""
    real = auto()
    """Real numbers."""
    text = auto()
    """
    Text/string that consists of individual characters.
    Allows substring search, concatenation and manipulation with register.
    """
    time = auto()
    """Time. `time_1 - time_0 = timedelta`."""
    timedelta = auto()
    """Timedelta. `time_0 + timedelta = time_1`."""


# TODO
class SemanticType(StrEnum):
    pass


class ValueConstraint(ABC):
    """
    Value constraint abstract base class.
    """

    def __init__(self, *args, **kwargs) -> None:
        pass

    @abstractmethod
    def is_valid(self, value) -> Union[bool, Any]:
        """
        Has a terse `__call__` alias:

        `value_constraint(value) == value_constraint.is_valid(value) $\\forall$ value`.

        Non-bool return-values are for specific implementation purposes -- please ignore.
        """
        return True

    def __call__(self, value) -> Union[bool, Any]:
        return self.is_valid(value)


class AnyValue(ValueConstraint):
    """
    Any value is valid value.

    >>> av = AnyValue()
    >>> av(1)
    True
    >>> av("asdf")
    True
    >>> import math
    >>> av(math.nan)
    True
    >>> av(AnyValue())
    True
    """

    def is_valid(self, value) -> bool:
        """"""  # (pdoc) removes inherited docstring
        return True


class And(ValueConstraint):
    """
    Valid value must satisfy all constraints.

    >>> r = And(NotEqual(1), NotEqual(2), NotEqual(3))
    >>> r(0)
    True
    >>> r(1)
    False
    >>> r(2)
    False
    >>> r(3)
    False
    >>> r(4)
    True

    >>> r = And(GreaterThan(1), LessThan(3))
    >>> r(0)
    False
    >>> # greater than is not strict by default
    >>> r(1)
    True
    >>> r(2)
    True
    >>> # less than is strict by default
    >>> r(3)
    False
    >>> r(4)
    False
    """

    def __init__(self, *args) -> None:
        if len(args) > 1:
            # args is a list of constraints
            self._constraints = args
        elif len(args) == 1:
            if isinstance(args[0], list):
                # args[0] is a list of constraints
                self._constraints = args[0]
            else:
                # args[0] is the only constraint
                self._constraints = [args[0]]
        else:
            # len(args) == 0
            self._constraints = []

    def is_valid(self, value) -> bool:
        """"""  # (pdoc) removes inherited docstring
        for r in self._constraints:
            if not r(value):
                return False
        return True


class Or(ValueConstraint):
    """
    Valid value must satisfy any of constraints.

    >>> r = Or(Equal(1), Equal(2), Equal(3))
    >>> r(0)
    False
    >>> r(1)
    True
    >>> r(2)
    True
    >>> r(3)
    True
    >>> r(4)
    False

    >>> r = Or(LessThan(1), GreaterThan(3))
    >>> r(0)
    True
    >>> # less than is strict by default
    >>> r(1)
    False
    >>> r(2)
    False
    >>> # greater than is not strict by default
    >>> r(3)
    True
    >>> r(4)
    True
    """

    def __init__(self, *args) -> None:
        if len(args) > 1:
            # args is a list of constraints
            self._constraints = args
        elif len(args) == 1:
            if isinstance(args[0], list):
                # args[0] is a list of constraints
                self._constraints = args[0]
            else:
                # args[0] is the only constraint
                self._constraints = [args[0]]
        else:
            # len(args) == 0
            self._constraints = []

    def is_valid(self, value) -> bool:
        """"""  # (pdoc) removes inherited docstring
        for r in self._constraints:
            if r(value):
                return True
        return False


class Not(ValueConstraint):
    """
    Negation.

    >>> r = Not(Equal(1))
    >>> r(0)
    True
    >>> r(1)
    False
    >>> r(2)
    True
    """

    def __init__(self, constraint: ValueConstraint) -> None:
        self._constraint = constraint

    def is_valid(self, value) -> bool:
        """"""  # (pdoc) removes inherited docstring
        return not self._constraint(value)


class Xor(ValueConstraint):
    """
    Valid value must satisfy uneven number of constraints.
    If `allow_uneven = True` valid value must satisfy exactly one constraint.

    >>> r = Xor(ValidRange(0, 2), ValidRange(1, 3))
    >>> r(-1)
    False
    >>> r(0)
    True
    >>> r(1)
    False
    >>> r(2)
    True
    >>> r(3)
    False
    """

    def __init__(self, *args, allow_uneven=True):
        self._allow_uneven = allow_uneven
        if len(args) > 1:
            self._constraints = args
        elif len(args) == 1:
            if isinstance(args[0], list):
                # args[0] is a list of constraints
                self._constraints = args[0]
            else:
                # args[0] is the only constraint
                self._constraints = [args[0]]
        else:
            # len(args) == 0
            self._constraints = []

    def is_valid(self, value) -> bool:
        """"""  # (pdoc) removes inherited docstring
        res = 0
        for r in self._constraints:
            res += int(r(value))
        if self._allow_uneven:
            return bool(res % 2)
        else:
            return res == 1


class Equal(ValueConstraint):
    """
    Only this value is valid value.

    >>> r = Equal(1)
    >>> r(0)
    False
    >>> r(1)
    True
    >>> r(2)
    False
    """

    def __init__(self, valid_value) -> None:
        self._valid_value = valid_value

    def is_valid(self, value) -> bool:
        """"""  # (pdoc) removes inherited docstring
        return value == self._valid_value


class IsIn(ValueConstraint):
    """
    Only these values are valid values.

    >>> r = IsIn(1, 2, 3)
    >>> r(0)
    False
    >>> r(1)
    True
    >>> r(2)
    True
    >>> r(3)
    True
    >>> r(4)
    False
    """

    def __init__(self, *args) -> None:
        if len(args) > 1:
            # args is a list of constraints
            self._constraints = args
        elif len(args) == 1:
            if isinstance(args[0], list):
                # args[0] is a list of constraints
                self._constraints = args[0]
            else:
                # args[0] is the only constraint
                self._constraints = [args[0]]
        else:
            # len(args) == 0
            self._constraints = []

    def is_valid(self, value) -> bool:
        """"""  # (pdoc) removes inherited docstring
        return Or([Equal(v) for v in self._constraints]).is_valid(value)


class NotEqual(ValueConstraint):
    """
    Any value except this value is valid value.

    >>> r = NotEqual(1)
    >>> r(0)
    True
    >>> r(1)
    False
    >>> r(2)
    True
    """

    def __init__(self, invalid_value) -> None:
        self._invalid_value = invalid_value

    def is_valid(self, value) -> bool:
        """"""  # (pdoc) removes inherited docstring
        return Not(Equal(self._invalid_value)).is_valid(value)


class IsNotIn(ValueConstraint):
    """
    Any value except these values is valid value.

    >>> r = IsNotIn(1, 2, 3)
    >>> r(0)
    True
    >>> r(1)
    False
    >>> r(2)
    False
    >>> r(3)
    False
    >>> r(4)
    True
    """

    def __init__(self, *args) -> None:
        if len(args) > 1:
            # args is a list of constraints
            self._constraints = args
        elif len(args) == 1:
            if isinstance(args[0], list):
                # args[0] is a list of constraints
                self._constraints = args[0]
            else:
                # args[0] is the only constraint
                self._constraints = [args[0]]
        else:
            # len(args) == 0
            self._constraints = []

    def is_valid(self, value) -> bool:
        """"""  # (pdoc) removes inherited docstring
        return And([NotEqual(v) for v in self._constraints]).is_valid(value)


class GreaterThan(ValueConstraint):
    """
    Valid value must be greater than this value.
    NOT STRICT (>=) by default.

    >>> r = GreaterThan(1)
    >>> r(0)
    False
    >>> r(1)
    True
    >>> r(2)
    True
    """

    def __init__(self, boundary, strict: bool = False) -> None:
        self._boundary = boundary
        self._strict = strict

    def is_valid(self, value) -> bool:
        """"""  # (pdoc) removes inherited docstring
        if self._strict:
            return value > self._boundary
        else:
            return value >= self._boundary


class LessThan(ValueConstraint):
    """
    Valid value must be less than this value.
    Strict (<) by default.

    >>> r = LessThan(1)
    >>> r(0)
    True
    >>> r(1)
    False
    >>> r(2)
    False
    """

    def __init__(self, boundary, strict: bool = True) -> None:
        self._boundary = boundary
        self._strict = strict

    def is_valid(self, value) -> bool:
        """"""  # (pdoc) removes inherited docstring
        return Not(GreaterThan(self._boundary, not self._strict)).is_valid(value)


class ValidRange(ValueConstraint):
    """
    Valid value must belong to [lo, hi) range, meaning `lo <= valid_value < hi`.
    Strictness of the boundaries is configurable.

    >>> r = ValidRange(1, 3)
    >>> r(0)
    False
    >>> r(1)
    True
    >>> r(2)
    True
    >>> r(3)
    False
    >>> r(4)
    False
    """

    def __init__(self, lo, hi, strict_lo: bool = False, strict_hi: bool = True) -> None:
        self._lo = lo
        self._hi = hi
        self._strict_lo = strict_lo
        self._strict_hi = strict_hi

    def is_valid(self, value) -> bool:
        """"""  # (pdoc) removes inherited docstring
        return And(
            GreaterThan(self._lo, self._strict_lo), LessThan(self._hi, self._strict_hi)
        ).is_valid(value)


class InvalidRange(ValueConstraint):
    """
    Valid value must not belong to [lo, hi) range, meaning either `valid_value < lo` or `valid_value >= hi`.
    Strictness of the boundaries is configurable.

    >>> r = InvalidRange(1, 3)
    >>> r(0)
    True
    >>> r(1)
    False
    >>> r(2)
    False
    >>> r(3)
    True
    >>> r(4)
    True
    """

    def __init__(self, lo, hi, strict_lo: bool = False, strict_hi: bool = True) -> None:
        self._lo = lo
        self._hi = hi
        self._strict_lo = strict_lo
        self._strict_hi = strict_hi

    def is_valid(self, value) -> bool:
        """"""  # (pdoc) removes inherited docstring
        return Not(
            ValidRange(self._lo, self._hi, self._strict_lo, self._strict_hi)
        ).is_valid(value)


class _Compose(ValueConstraint):
    """
    Compose value constraints.
    This is a workaround to implement length constraint for strings.
    We can override `is_valid` semantics to return int, not bool.
    Then we can pass this int to other value constraints and eventually get bool.

    >>> r = _Compose(Equal(2), _Length())
    >>> r("a")
    False
    >>> r("aa")
    True
    >>> r("aaa")
    False
    """

    def __init__(self, *args, backward: bool = True) -> None:
        self._backward = backward
        if len(args) > 1:
            # args is a list of constraints
            self._constraints = args
        elif len(args) == 1:
            if isinstance(args[0], list):
                # args[0] is a list of constraints
                self._constraints = args[0]
            else:
                # args[0] is the only constraint
                self._constraints = [args[0]]
        else:
            # len(args) == 0
            self._constraints = []

    def is_valid(self, value) -> bool:
        if not self._backward:
            for r in self._constraints:
                value = r.is_valid(value)
        else:
            for r in reversed(self._constraints):
                value = r.is_valid(value)
        return value


class _Length(ValueConstraint):
    """
    Compute length.
    `is_valid` returns int, not bool.

    >>> r = _Length()
    >>> r("a")
    1
    >>> r("aa")
    2
    >>> r("aaa")
    3
    """

    def is_valid(self, value) -> int:
        """"""  # (pdoc) removes inherited docstring
        return len(value)


class LengthEqual(ValueConstraint):
    """
    >>> r = LengthEqual(2)
    >>> r("a")
    False
    >>> r("aa")
    True
    >>> r("aaa")
    False
    """

    def __init__(self, valid_length) -> None:
        self._valid_length = valid_length

    def is_valid(self, value) -> bool:
        """"""  # (pdoc) removes inherited docstring
        return _Compose(Equal(self._valid_length), _Length()).is_valid(value)


class LengthGreaterThan(ValueConstraint):
    """
    Value is valid if its length is greater than specified.
    NOT STRICT (>=) by default.

    >>> r = LengthGreaterThan(2)
    >>> r("a")
    False
    >>> r("aa")
    True
    >>> r("aaa")
    True
    """

    def __init__(self, boundary: int, strict: bool = False) -> None:
        self._boundary = boundary
        self._strict = strict

    def is_valid(self, value) -> bool:
        """"""  # (pdoc) removes inherited docstring
        return _Compose(GreaterThan(self._boundary, self._strict), _Length()).is_valid(
            value
        )


class LengthLessThan(ValueConstraint):
    """
    Value is valid if its length is less than specified.
    Strict (<) by default.

    >>> r = LengthLessThan(2)
    >>> r("a")
    True
    >>> r("aa")
    False
    >>> r("aaa")
    False
    """

    def __init__(self, boundary: int, strict: bool = True) -> None:
        self._boundary = boundary
        self._strict = strict

    def is_valid(self, value) -> bool:
        """"""  # (pdoc) removes inherited docstring
        return _Compose(LessThan(self._boundary, self._strict), _Length()).is_valid(
            value
        )


class LengthValidRange(ValueConstraint):
    """
    Value is valid if its length belongs to [lo, hi) range, meaning `lo <= len(valid_value) < hi`.
    Strictness of the boundaries is configurable.

    >>> r = LengthValidRange(1, 3)
    >>> r("")
    False
    >>> r("a")
    True
    >>> r("aa")
    True
    >>> r("aaa")
    False
    >>> r("aaaa")
    False
    """

    def __init__(
        self, lo: int, hi: int, strict_lo: bool = False, strict_hi: bool = True
    ) -> None:
        self._lo = lo
        self._hi = hi
        self._strict_lo = strict_lo
        self._strict_hi = strict_hi

    def is_valid(self, value) -> bool:
        """"""  # (pdoc) removes inherited docstring
        return _Compose(
            ValidRange(self._lo, self._hi, self._strict_lo, self._strict_hi), _Length()
        ).is_valid(value)


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.ELLIPSIS)
