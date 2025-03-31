import pandas as pd

from atptools.process_components import pandas_counter_reset_detector

dfts = pd.DataFrame(
    data={
        "name": [
            "value_1",
            "value_1",
            "value_1",
            "value_1",
            "value_1",
            "value_1",
            "value_1",
        ],
        "value": [1, 2, 3, 1.2, 2, 0, 2],
    },
    index=pd.date_range("2021-01-01", "2021-01-05", periods=7),
)

list_1, list_2 = pandas_counter_reset_detector(dfts["value"])
print(list_1)
print(list_2)
