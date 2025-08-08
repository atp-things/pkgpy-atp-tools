import io
from pprint import pprint

import pandas as pd

import atptools

# read the CSV file
with open("data/data.csv") as f:
    ds_string = f.read()

df, _ = atptools.csv.csv_str_to_dataframe(ds_string)

print("df:", df)
print("metadata:", df.attrs)
