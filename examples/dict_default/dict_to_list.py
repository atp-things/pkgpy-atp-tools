import datetime
import uuid
from pprint import pprint

from atptools import DictDefault

# DictDefault---------------------------------------------------------------
def_dict = DictDefault()

def_dict["name0"] = "text 1"
def_dict["name"]["value1"] = "text 1"
def_dict["name"]["value2"] = "text 2"
def_dict["name2"]["list_num"] = [1, 2, 3, 4, 5]
def_dict["name2"]["list_string"] = ["a", "b", "c", "d", "e"]
def_dict["name2"]["list_dict"] = [{"a": 1}, {"b": 2}, {"c": 3}, {"d": 4}, {"e": 5}]
def_dict["name2"]["list_list"] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def_dict["name2"]["dict"] = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
def_dict["name3"]["uuid"] = uuid.uuid4()
def_dict["name3"]["datetime_utc"] = datetime.datetime.now(datetime.UTC)
def_dict["name3"]["timestamp_utc"] = datetime.datetime.now(datetime.UTC).timestamp()

pprint(dict(def_dict))

keys = [
    ["name0"],
    ["name2", "list_num"],
    ["name3", "uuid"],
]
values = def_dict.to_vector(keys=keys, flatten=True)
print("keys: ")
pprint(keys)
print("values: ")
pprint(values)
