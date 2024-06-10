from pathlib import Path
from pprint import pprint

from atpdataset import DictDefault, Records

# DictDefault---------------------------------------------------------------
records = Records()
records.from_json(Path("data_sample", "records", "test1.json"))

print("records [type]", type(records))
pprint(records)

print("records to dict [level 1]:")
pprint(records.to_dict(["first_name"]))
print("records to dict [level 2]:")
pprint(records.to_dict(["first_name", "last_name"]))

dict_default = DictDefault()
dict_default.from_dict(records.to_dict(["first_name", "last_name"]))
print("dict_default [type]", type(dict_default))
pprint(dict_default)
dict_default.to_json(Path("data", "records", "test1_output.json"))
