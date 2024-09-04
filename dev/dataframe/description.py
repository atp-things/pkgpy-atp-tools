from pprint import pprint

import numpy as np
import pandas as pd
from atptools.dataframe import df_description_dict_default, df_description_str

df = pd.DataFrame(
    {
        "A": [1, 2, 3],
        "B": [4, 5, 6],
        "C": ["7", "8", "9"],
        "E": [np.nan, 5, 6],
        "F": [np.nan, np.nan, 6],
        "G": [np.nan, np.nan, None],
    }
)
print("Dataframe:")

print(df_description_str(df))
print("Json:")
pprint(df_description_dict_default(df))
