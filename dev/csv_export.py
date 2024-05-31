import atpdataset
import pandas as pd

print("This is a test of the atpdataset package")
print("Name:", atpdataset.__name__)
print("Version:", atpdataset.__version__)

data: dict = {
    "first_name": ["John", "Jane"],
    "last_name": ["Doe", "Smith"],
    "age": [30, 25],
    "city": ["New York", "San Francisco"],
}
metadata: dict = {"name": "Sample test", "author": "andrazpolak"}
df = pd.DataFrame(data)
print(df)
# convert the DataFrame to a CSV buffer
# csv_buffer = df.to_csv(index=False)
csv_buffer = atpdataset.csv.dataframe_to_csv_str(df, metadata)
# write the CSV buffer to a file
with open("data/data.csv", "w") as f:
    f.write(csv_buffer)

df.attrs = metadata
csv_buffer_v2 = atpdataset.csv.dataframe_to_csv_str(df)
with open("data/data_v2.csv", "w") as f:
    f.write(csv_buffer_v2)
