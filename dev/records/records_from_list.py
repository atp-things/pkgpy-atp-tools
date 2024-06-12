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
dict_3 = records.to_dict_default(["first_name", "last_name", "age"])
print("type(dict_3)", type(dict_3))
pprint(dict_3)
dict_4 = records.to_dict(["first_name", "last_name", "age"])
print("type(dict_4)", type(dict_4))
pprint(dict_4)

dict_5 = records.to_defaultdict(["first_name", "last_name", "age"])
print("type(dict_5)", type(dict_5))
pprint(dict_5)

df = records.to_dataframe(index=["first_name", "last_name"], columns=["email"])
print("df [type]", type(df))
print(df)
