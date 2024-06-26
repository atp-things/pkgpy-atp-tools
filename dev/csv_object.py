from atptools import AtpDataset

# read the CSV file
path = "data/data.csv"

ads = AtpDataset()
ads.from_csv_file(path)


print("df:", ads.df)
print("metadata_1:", ads.metadata)
print("metadata_2:", ads.df.attrs)
print("name:", ads.name)
print("name:", ads.uuid)
