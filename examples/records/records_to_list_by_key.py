from pathlib import Path
from pprint import pprint

from atptools import DictDefault, Records

# DictDefault---------------------------------------------------------------
records = Records()
records.from_json(Path("data_sample", "records", "test1.json"))

# print("records [type]", type(records))
# pprint(records)

print("Output")
pprint(records.to_list_by_key("last_name"))
