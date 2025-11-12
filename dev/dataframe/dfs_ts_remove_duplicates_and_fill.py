import numpy as np
import pandas as pd

from atptools.dataframe.series_ts import remove_duplicates_and_fill

number_list: list[float] = [1.0, 1, 1, 1, 0.0, 1.0, 1, 1, 1, 1.0, 0.0, 0, 2, 2, 2, 2]
dfs = pd.Series(
    number_list,
    index=pd.date_range(
        "2024-01-01",
        periods=len(number_list),
        freq="T",
    ),
)

dfs_2: pd.Series = remove_duplicates_and_fill(dfs)
print(dfs_2)
