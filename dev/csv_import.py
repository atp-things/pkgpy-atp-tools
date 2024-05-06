import io
from pprint import pprint

import pandas as pd

import atpdataset

# read the CSV file
with open("data/data.csv", "r") as f:
    ds_string = f.read()

df, _ = atpdataset.csv.csv_str_to_dataframe(ds_string)

print("df:", df)
print("metadata:", df.attrs)
