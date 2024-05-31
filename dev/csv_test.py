import csv
from pathlib import Path
from pprint import pprint

print("Test csv")
file_path = Path("data", "test_write").with_suffix(".csv")

# save data to csv
with open(file_path, "w", newline="") as csvfile:
    fieldnames = ["first_name", "extra", "last_name"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({"first_name": "Baked", "extra": 1.4, "last_name": "Beans"})
    writer.writerow({"first_name": "Lovely", "last_name": "Spam"})
    writer.writerow({"first_name": "Wonderful", "last_name": "Spam"})


# read data from csv
with open(file_path) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        pprint(row)


# sniff dialect
with open(file_path) as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    print("Dialect: ")
    print("  delimiter: ", dialect.delimiter)
    print("  quoting: ", dialect.quoting)
    print("  quotechar: ", dialect.quotechar)
    print("  doublequote: ", dialect.doublequote)
    print("  escapechar: ", dialect.escapechar)
    reader = csv.reader(csvfile, dialect)
    for row in reader:
        pprint(row)
