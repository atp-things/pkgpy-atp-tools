from pprint import pprint

from pydantic import BaseModel, TypeAdapter

from atptools import Records


class User(BaseModel):
    first_name: str
    last_name: str
    age: int
    email: str


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


records_1 = Records(record_list, pydantic_model=User)
records_2 = Records(record_list)
records_2.validate_pydantic(pydantic_model=User)
