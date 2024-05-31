import datetime
import uuid
from pathlib import Path
from pprint import pprint

from atpdataset import Dict, DictDefault

# DictDefault---------------------------------------------------------------
def_dict = DictDefault()
def_dict["name"]["value1"] = "text 1"
def_dict["name"]["value2"] = "text 2"
def_dict["name2"]["list_num"] = [1, 2, 3, 4, 5]
def_dict["name2"]["list_string"] = ["a", "b", "c", "d", "e"]
def_dict["name2"]["list_dict"] = [{"a": 1}, {"b": 2}, {"c": 3}, {"d": 4}, {"e": 5}]
def_dict["name2"]["list_list"] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def_dict["name2"]["dict"] = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
def_dict["name3"]["uuid"] = uuid.uuid4()
def_dict["name3"]["datetime_utc"] = datetime.datetime.now(datetime.timezone.utc)
def_dict["name3"]["timestamp_utc"] = datetime.datetime.now(
    datetime.timezone.utc
).timestamp()

print(
    "def_dict [json]:",
    def_dict.to_json(Path("data", "tesst_export_dict_default.json"), indent=2),
)
print(
    "def_dict [yaml]:",
    def_dict.to_yaml(Path("data", "tesst_export_dict_default.yaml")),
)
print(
    "def_dict [toml]:",
    def_dict.to_toml(Path("data", "tesst_export_dict_default.toml")),
)
pprint(dict(def_dict))
# Dict -----------------------------------------------------------------------
config = Dict(
    {
        "name": {"value1": "text 1", "value2": "text 2"},
        "name2": {
            "list_num": [1, 2, 3, 4, 5],
            "list_string": ["a", "b", "c", "d", "e"],
            "list_dict": [{"a": 1}, {"b": 2}, {"c": 3}, {"d": 4}, {"e": 5}],
            "list_list": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            "dict": {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5},
        },
        "name3": {
            "uuid": uuid.uuid4(),
            "datetime_utc": datetime.datetime.now(datetime.timezone.utc),
            "timestamp_utc": datetime.datetime.now(datetime.timezone.utc).timestamp(),
        },
    }
)

print("Dict type:", type(config))


print("config [json]:", config.to_json(Path("data", "tesst_export_dict"), indent=2))
print("config [yaml]:", config.to_yaml(Path("data", "tesst_export_dict.yaml")))
print("config [toml]:", config.to_toml(Path("data", "tesst_export_dict.toml")))
