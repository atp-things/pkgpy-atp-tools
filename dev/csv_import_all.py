import io
import json
from pathlib import Path
from pprint import pprint

import atpdataset
import pandas as pd

# import all .csv files from folder data_sample
# list all files in the folder data_sample
folder_dir = "data_sample"
file_extension = ["*metadata.json"]
files_metadata = [f for ext in file_extension for f in Path(folder_dir).glob(ext)]
datasets_metadata: list[dict] = []

for file in files_metadata:
    with open(file) as f:
        metadata = f.read()
        metadata_dict: dict = json.loads(metadata)
        metadata_dict["data_file_path"] = str(file).replace(".metadata.json", ".csv")
        datasets_metadata.append(metadata_dict)

for metadata in datasets_metadata:
    with open(metadata["data_file_path"]) as f:
        ds_string = f.read()

    df, _ = atpdataset.csv.csv_str_to_dataframe(ds_string)

    print("df:", df)
    print("df description:", df.describe().T)
    print("metadata:", df.attrs)
