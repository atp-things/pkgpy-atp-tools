import numpy as np
import pandas as pd

from atptools.dataframe.index import datetimeindex_to_seconds_array

pd_index: pd.DatetimeIndex = pd.DatetimeIndex(
    [
        "2023-01-01 00:00:00",
        "2023-01-01 00:00:01",
        "2023-01-01 00:00:02",
        "2023-01-01 00:00:03",
    ]
)
seconds_array: np.ndarray = datetimeindex_to_seconds_array(pd_index)
print("DatetimeIndex to seconds array:")
print(seconds_array)
