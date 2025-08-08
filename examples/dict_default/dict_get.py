from pathlib import Path
from pprint import pprint

from atptools import DictDefault

# DictDefault---------------------------------------------------------------
def_dict = DictDefault()
def_dict.from_file(Path("data_sample", "dict_test", "test1.json"))

print("def_dict")
pprint(def_dict)
print("name:", def_dict["name"])
print("name [get]:", def_dict.get("name"))
print("name [get-None]:", def_dict.get("namesd"))
