from pathlib import Path
from pprint import pprint

from atpdataset import DictDefault, Records

record_list: list[dict] = [
    {
        "first_name": "Sherlock",
        "last_name": "Holmes",
        "age": 45,
        "email": "sherlock.holmes@gmail.com",
    },
    {
        "first_name": "John",
        "last_name": "Watson",
        "age": 50,
        "email": "john.watson@gmail.com",
    },
    {
        "first_name": "John",
        "last_name": "Malcovich",
        "age": 50,
        "email": "john.malcovich@gmail.com",
    },
    {
        "first_name": "Agatha",
        "last_name": "Christie",
        "age": 60,
        "email": "agatha.christie@gmail.com",
    },
]


records = Records(record_list)


print("records [type]", type(records))
pprint(records)

print("records to dict [level 1]:")
# pprint(records.to_dict(["first_name"]))
print("records to dict [level 2]:")
pprint(records.to_dict(["first_name", "last_name"]))
print("records to dict [level 3]:")
pprint(records.to_dict(["first_name", "last_name", "age"]))

# dict_default = DictDefault()
# dict_default.from_dict(records.to_dict(["first_name", "last_name"]))
# print("dict_default [type]", type(dict_default))
# pprint(dict_default)
# dict_default.to_json(Path("data", "records", "test1_output.json"))
