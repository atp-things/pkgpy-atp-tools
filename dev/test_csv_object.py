import io
from pathlib import Path

import atpdataset

file_path = Path("data_sample", "a95a4758-a57c-45c9-8930-9f63613e7467.csv")

csv_object = atpdataset.Csv()
# csv_object.read_file(file_path)


with io.open(file_path, "rb") as f:
    data = f.read()
    # print("data type: ", type(data))
    csv_object.read_buffer(io.BytesIO(data))

# print("data_bytes type: ", type(data_bytes))
# csv_object.read_buffer(data_bytes)
