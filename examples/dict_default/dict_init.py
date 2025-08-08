from pprint import pprint

from atptools import DictDefault

# DictDefault---------------------------------------------------------------
def_dict = DictDefault(
    {
        "name": {
            "value1": "text 1",
            "value2": "text 2",
        },
        "urnam": {},
        "nam2e": {
            "value1": "text 1",
            "value2": "text 2",
        },
    }
)

pprint(def_dict.to_dict())
