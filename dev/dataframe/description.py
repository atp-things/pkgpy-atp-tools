import numpy as np
import pandas as pd
from atptools.dataframe import (
    df_description_str,
)

df = pd.DataFrame(
    {
        "A": [1, 2, 3],
        "B": [4, 5, 6],
        "C": ["7", "8", "9"],
        "E": [np.nan, 5, 6],
    }
)
# print("Dataframe:")
# print(df)
print("Str:")
print(df_description_str(df))
# print("Json:")
# pprint(df_description_json(df))
# print("Markdown:")
# print(df_description_markdown(df))
