from pprint import pprint

from atptools import Records

record_list = [
    {
        "first_name": "Sherlock",
        "last_name": "Holmes",
        "age": 45,
        "value1": {"value2": "text 2"},
        "list": [1, 2, 5],
        "email": "sherlock.holmes@gmail.com",
    },
    {
        "first_name": "John",
        "last_name": "Watson",
        "age": 50,
        "value1": {"value2": "text 2"},
        "list": [1, 2, 3],
        "email": "john.watson@gmail.com",
    },
    {
        "first_name": "John",
        "last_name": "Malcovich",
        "age": 50,
        "value1": {"value2": "text 2"},
        "list": [1, 2, 3],
        "email": "john.malcovich@gmail.com",
    },
    {
        "first_name": "Agatha",
        "last_name": "Christie",
        "age": 60,
        "value1": {"value2": "text 2"},
        "list": [1, 2, 2],
        "email": "agatha.christie@gmail.com",
    },
]


records = Records(record_list)
pprint(records)

keys = ["first_name", "list", "age", ["value1", "value2"], "email"]
vectors = records.to_vectors(keys=keys, flatten=True)
pprint(vectors)

vectors2 = records.to_vectors()
pprint(vectors2)
