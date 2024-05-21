import csv
from pathlib import Path
from pprint import pprint

# list all csv files in the public folder
folder_public = Path("data_sample")
folder_private = Path("data", "data_sample")
csv_files = list(folder_public.glob("*.csv")) + list(folder_private.glob("*.csv"))

pprint(csv_files)


for file_path in csv_files:
    print(file_path)
    with open(file_path, "r") as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        print("Dialect: ")
        print("  delimiter: ", dialect.delimiter)
        print("  quoting: ", dialect.quoting)
        print("  quotechar: ", dialect.quotechar)
        print("  doublequote: ", dialect.doublequote)
        print("  escapechar: ", dialect.escapechar)
        reader = csv.reader(csvfile, dialect)
        # for row in reader:
        #     pprint(row)
