import numpy as np
import pandas as pd

from atptools.dataframe.series_ts import remove_consecutive_duplicates

pd_index: pd.DatetimeIndex = pd.DatetimeIndex(
    [
        "2023-01-01 00:00:00",
        "2023-01-01 00:00:01",
        "2023-01-01 00:00:02",
        "2023-01-01 00:00:03",
    ]
)
dfs: pd.Series = pd.Series(
    [10, 10, 20, 20],
    index=pd_index,
)

dfs_2: pd.Series = remove_consecutive_duplicates(dfs)
print(dfs_2)
