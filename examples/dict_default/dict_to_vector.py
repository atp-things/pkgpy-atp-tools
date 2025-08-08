from pprint import pprint

from atptools import DictDefault

# DictDefault---------------------------------------------------------------
dict_input = {
    "first_name": "Agatha",
    "last_name": "Christie",
    "age": 60,
    "value1": {"value2": "text 2"},
    "list": [1, 2, 2],
    "email": "agatha.christie@gmail.com",
}

def_dict = DictDefault()
def_dict.from_dict(dict_input)

print("def_dict")
pprint(def_dict)
print("vector_1:")
pprint(def_dict.to_vector())


print("vector_2:")
pprint(def_dict.to_vector(keys=["first_name", "list", "age"]))


print("vector_3:")
pprint(def_dict.to_vector(keys=["first_name", "list", "age"], flatten=True))
