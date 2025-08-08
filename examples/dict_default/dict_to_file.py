from pathlib import Path
from pprint import pprint

from atptools import DictDefault

# DictDefault---------------------------------------------------------------
dict_default = DictDefault()
dict_default.from_json(Path("data_sample", "dict_test", "test1.json"))
dict_default.to_json(Path("data", "output", "dict_default_test1.json"), indent=2)
dict_default.to_yaml(Path("data", "output", "dict_default_test1.yaml"))
dict_default.to_toml(Path("data", "output", "dict_default_test1.toml"))


print("dict_default")
pprint(dict_default)
