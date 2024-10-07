from pathlib import Path
from pprint import pprint

import atptools
import pandas as pd

df = pd.read_csv(Path("data_sample", "dataset_ts_long", "test1.csv"))

datset_stl = atptools.AtpDatasetTsLong()
print("df1")
print(datset_stl.df)
datset_stl.add_dataframe(df, name_col="id")

metadata_series = atptools.Records([{"name": "test2", "unit": "unit"}])
pprint(metadata_series)


print("df2")
print(datset_stl.to_dataframe())
dfs = pd.Series(
    [1, 2, 3, 4, 5],
    index=pd.date_range("2021-01-01", "2021-01-05", periods=5),
    name="test1",
)
datset_stl.add_series(
    dfs,
    "test2",
)
print("df3")
print(datset_stl.to_dataframe())
print("index")
print(datset_stl.df.index)

print("get_time_range")
print(datset_stl.get_time_range())
datset_stl.update_metadata_series(metadata_series)
print("metadata")
pprint(datset_stl.metadata_series)
