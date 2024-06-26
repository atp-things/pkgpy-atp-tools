from pathlib import Path
from pprint import pprint

from atptools import DictDefault

# DictDefault---------------------------------------------------------------
def_dict = DictDefault()
# def_dict.from_json(Path("data_sample", "dict_test", "test1.json"))
# def_dict.from_yaml(Path("data_sample", "dict_test", "test1.yaml"))
# def_dict.from_toml(Path("data_sample", "dict_test", "test1.toml"))
def_dict.from_file(Path("data_sample", "dict_test", "test1.json"))

print("def_dict")
pprint(def_dict)
