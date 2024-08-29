from pathlib import Path
from pprint import pprint

from atptools import DictDefault, Records

# DictDefault---------------------------------------------------------------
records = Records()
records.from_json(Path("data_sample", "records", "test1.json"))

# print("records [type]", type(records))
# pprint(records)

print("Output")
# pprint(records.group_by_tuplekey(["first_name", "last_name"]))
print("Output [key as tuple]")
pprint(dict(records.group_by(["first_name", "last_name"], key_as_tuple=True)))
print("Output [key as string]")
pprint(dict(records.group_by(["first_name"])))
