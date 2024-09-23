import csv
import datetime
import os
import pickle
import subprocess
from pathlib import Path

from schemaorg import logger as scl
from schemaorg import main as scm
from tqdm.auto import tqdm

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
    dttm = datetime.datetime.now(tz=datetime.timezone.utc)
    heading = (
        '"""\n'
        f"This file was automatically generated at {dttm.isoformat(sep=' ', timespec='seconds')}.\n"
        "\n"
        "Documentation may not function properly.\n"
        "\n"
        "Bindings for [schema.org types](https://schema.org/docs/full.html).\n"
        '"""\n'
        '__docformat__ = "numpy"\n'
        "\n"
        "import pickle\n"
        "from typing import Type\n"
        "\n"
        "import schemaorg.main\n"
        "\n"
        "Schema: Type = schemaorg.main.Schema\n"
    )
    if not Path(csv_path).is_file():
        load_types()
    types = read_csv(csv_path, keyfield="label")
    msg_lvl = scl.message.bot.level
    if not Path(binding_storage).is_file():
        storage_dict = dict()
        scl.message.bot.level = scl.message.WARNING
        from sys import getsizeof

        for t in tqdm(types):
            sanity_check = scm.Schema(t)
            storage_dict[t] = sanity_check
        scl.message.bot.level = msg_lvl
        with open(binding_storage, "wb") as sf:
            pickle.dump(storage_dict, sf)
    else:
        with open(binding_storage, "rb") as sf:
            storage_dict = pickle.load(sf)
    with open(binding_path, "w") as of:
        print(heading, file=of)
        print(f'with open("{binding_storage}", "rb") as sf:', file=of)
        print("    schema_storage = pickle.load(sf)", file=of)
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
            "        return getattr(sc, tkns[-1])\n",
            file=of,
        )
        for t in types:
            if t.isidentifier() and t != str(True) and t != str(False):
                print(f'    {t} = schema_storage["{t}"]', file=of)
                print(f'    """{storage_dict[t].comment}"""', file=of)
            else:
                print(f"{t} is not a valid identifier T_T")
                if ("_" + t).isidentifier():
                    print(f"    It was replaced with {'_' + t}")
                    print(f"    {'_' + t} = schema_storage[\"{t}\"]", file=of)
                    print(f'    """@public {storage_dict[t].comment}"""', file=of)
                else:
                    print("    Can't fix, skipping...")
        print("del schema_storage", file=of)
        # with open(os.devnull, "w") as devnull:
        #     if subprocess.call(["python", "-c", "import black"], stderr=devnull) == 0:
        #         print(f"{subprocess.call(["python", "-m", "black", binding_path])}")
        #     else:
        #         print("black not available, skipping...")
