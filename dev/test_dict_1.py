from pathlib import Path
from pprint import pprint

from atpdataset import Dict, DictDefault

# output_path = Path("data", "tesst_export").with_suffix(".json")
output_path = Path("data", "tesst_export")

def_dict = DictDefault()
def_dict["name"]["fdrs"] = "atpdataset"
def_dict["name"]["fds"] = "atpdataset"

print("def_dict:", def_dict.to_json())
pprint(dict(def_dict))

config = Dict()
config["name"] = "ffgftrt11dgfdsd"

print("config:", config.to_json(output_path))
