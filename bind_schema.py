import csv
import datetime
import os
import pickle
import re
import subprocess
from pathlib import Path

from schemaorg import logger as scl
from schemaorg import main as scm
from tqdm.auto import tqdm

# idiomatically, these should be parameters
project = "smlc"
root = "smlc"
csv_url = "https://raw.githubusercontent.com/openschemas/schemaorg/refs/heads/master/schemaorg/data/releases/12.0/schemaorg-all-http-types.csv"
csv_path = "schemaorg-all-http-types.csv"
# This is a relative path!!! Copy file for actual usage!!!
binding_storage = "schemaorg_types_storage.pkl"
binding_path = "schemaorg_types_binding.py"


def load_types():
    from shutil import copyfileobj
    from urllib import request

    with request.urlopen(csv_url) as r, open(csv_path, "wb") as f:
        copyfileobj(r, f)


# taken from https://github.com/openschemas/schemaorg/blob/master/schemaorg/utils.py
def read_csv(filename, mode="r", delim=",", header=None, keyfield=None):
    """
    taken from https://github.com/openschemas/schemaorg/blob/master/schemaorg/utils.py

    read a comma separated value file, with default delimiter as comma.
    we assume reading a header, and use some identifier as key.

    Parameters
    ==========
    filename: the name of the csv file to read
    mode: the mode to read in (defaults to r)
    delim: the delimiter (defaults to comma)
    """
    if not os.path.exists(filename):
        bot.exit("%s does not exist." % filename)

    # If we have a keyfield, return dictionary
    data = []
    if keyfield is not None:
        data = dict()

    with open(filename, mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file, fieldnames=header)
        for row in csv_reader:
            if keyfield is not None:
                data[row[keyfield]] = row
            else:
                data.append(row)
    return data


if __name__ == "__main__":
    binding_storage_path = os.path.join(root, binding_storage)
    binding_path = os.path.join(root, binding_path)
    local_link_corrector = re.compile(
        r'(<a class="localLink" href=")(/)(\w+)(">\3</a>)'
    )
    dttm = datetime.datetime.now(tz=datetime.timezone.utc)
    heading = (
        '"""\n'
        f"This file was automatically generated at {dttm.isoformat(timespec='seconds')}.\n"
        "\n"
        "Documentation may not function properly.\n"
        "\n"
        "Bindings for [schema.org types](https://schema.org/docs/full.html).\n"
        '"""\n'
        '__docformat__ = "numpy"\n'
        "\n"
        "from copy import deepcopy\n"
        "import os\n"
        "import pickle\n"
        "from typing import Type, Union\n"
        "\n"
        "import schemaorg.main\n"
        "\n"
        "Schemaorg: Type = schemaorg.main.Schema\n"
        "\n"
        "\n"
        "def _copyattrs(dst, src):\n"
        "    for an, av in vars(src).items():\n"
        "        setattr(dst, an, deepcopy(av))\n"
        "    return dst\n"
        "\n"
        "\n"
        "class Schema(Schemaorg):\n"
        '    """Wrapper for `Schemaorg`. Prepends "sc:" to formatted type names."""\n'
        "    def __init__(self, schema: Union[str, schemaorg.main.Schema], *args, **kwargs):\n"
        "        if isinstance(schema, schemaorg.main.Schema):\n"
        "            schelf = schema\n"
        "        else:\n"
        "            schelf = schemaorg.main.Schema(schema, *args, **kwargs)\n"
        "        _copyattrs(self, schelf)\n"
        "\n"
        "    def __str__(self):\n"
        '        return "sc:" + super(Schema, self).__str__()\n'
        "\n"
        "    def __repr__(self):\n"
        "        return str(self)\n"
        "\n"
        "\n"
    )
    if not Path(csv_path).is_file():
        load_types()
    types = read_csv(csv_path, keyfield="label")
    msg_lvl = scl.message.bot.level
    if not Path(binding_storage_path).is_file():
        storage_dict = dict()
        scl.message.bot.level = scl.message.WARNING
        from sys import getsizeof

        for t in tqdm(types):
            sanity_check = scm.Schema(t)
            storage_dict[t] = sanity_check
        scl.message.bot.level = msg_lvl
        with open(binding_storage_path, "wb") as sf:
            pickle.dump(storage_dict, sf)
    else:
        with open(binding_storage_path, "rb") as sf:
            storage_dict = pickle.load(sf)
    with open(binding_path, "w") as of:
        print(heading, file=of)
        print(
            f'with open(os.path.join("{root}", "{binding_storage}"), "rb") as sf:',
            file=of,
        )
        print("    schema_storage = pickle.load(sf)", file=of)
        print("\n", file=of)
        print("class sc:", file=of)
        print('    """', file=of)
        print(
            '    Convenient namespace. Usage: `sc.TypeName` instead of `Schema("TypeName")`.',
            file=of,
        )
        print(file=of)
        print(
            "    Special cases: `_True`, `_False` and `_3DModel` are prepended with `_` for pythonic reasons.",
            file=of,
        )
        print('    """', file=of)
        print(
            "    def parse(tn: str, sep=':', raise_not_sc: bool = True):\n"
            '        """`\'sc:TypeName\'` to `sc.TypeName`"""\n'
            '        tkns = tn.split(":")\n'
            "        if raise_not_sc:\n"
            '            assert tkns[0] == "sc", "Type annotation must start with \'sc:\'"\n'
            "        t = tkns[-1]\n"
            '        if t in ["True", "False", "3DModel"]:\n'
            '            t = "_" + t\n'
            "        return getattr(sc, t)\n",
            file=of,
        )
        for t in types:
            comment = storage_dict[t].comment
            comment, _ = local_link_corrector.subn(r"\1#sc.\3\4", comment)
            if t.isidentifier() and t != str(True) and t != str(False):
                print(f'    {t} = Schema(schema_storage["{t}"])', file=of)
                print(f'    """{comment}"""', file=of)
            else:
                print(f"{t} is not a valid identifier T_T")
                if ("_" + t).isidentifier():
                    print(f"    It was replaced with {'_' + t}")
                    print(f"    {'_' + t} = Schema(schema_storage[\"{t}\"])", file=of)
                    print(f'    """@public {comment}"""', file=of)
                else:
                    print("    Can't fix, skipping...")
        print("\n", file=of)
        print("del schema_storage", file=of)
