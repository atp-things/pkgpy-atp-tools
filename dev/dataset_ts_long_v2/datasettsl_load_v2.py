from pathlib import Path
from pprint import pprint

import pandas as pd

from atptools import AtpDatasetTsLongV2

df = pd.read_csv(Path("data_sample", "dataset_ts_long", "test1.csv"))
df = df.rename(columns={"datetime": "dt", "value": "value"})
print("df:", df)


atp_df_long = AtpDatasetTsLongV2(
    columns={
        "id": {"index": True, "type": "str"},
        "id2": {"type": "str"},
    },
).add_dataframe(df)
df_long = atp_df_long.to_dataframe()
print("df_long:", df_long)
# print("description:", atp_df_long.get_dataframe_description())
df2 = pd.DataFrame(
    {
        "id": ["value_name_2", "value_name_3"],
        "id2": ["sdfdsfdsf", "fdsfsdfds"],
        "dt": [
            "2024-09-01 00:09:53",
            "2023-10-01 00:00:00",
        ],
        "value": [1, 2],
    }
)
atp_df_long.add_dataframe(df2)
print("df_long2:", atp_df_long.df)
