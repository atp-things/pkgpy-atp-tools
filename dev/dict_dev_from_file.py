import datetime
import uuid
from collections import defaultdict
from pathlib import Path
from pprint import pprint

from atpdataset import Dict, DictDefault

# DictDefault---------------------------------------------------------------
def_dict = DictDefault()
# def_dict.from_json(Path("data_sample", "dict_test", "test1.json"))
# def_dict.from_yaml(Path("data_sample", "dict_test", "test1.yaml"))
def_dict.from_toml(Path("data_sample", "dict_test", "test1.toml"))

print("def_dict")
pprint(def_dict)

print("datetime_utc:", def_dict["name3"]["datetime_utc"])
print("datetime_utc [type]:", type(def_dict["name3"]["datetime_utc"]))
print("uuid [type]:", type(def_dict["name3"]["uuid"]))
