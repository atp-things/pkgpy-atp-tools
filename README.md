# pkgpy-atp-tools

Simple tools for data manipulation.

## URLs

- [GitHub](https://github.com/atp-things/pkgpy-atp-tools)
- [PyPI](https://pypi.org/project/atptools/)

## Installation

### From PyPI

```bash
pip install atptools
```

```bash
pipenv install atptools
```

## Content

### File io (async)

### Records

### DictDefault

### Dataset

Dataset is collection of data.
Variable (name of data point):
Records: Collection of data points.
Data point: Single piece of information. Temperature, humidity, location etc.

### Dataset Timeseries

#### Metadata

- dataset:
  - uuid
  - name
  - description
  - source
  - variables:

#### Longformat

columns:

- datetime or timestamp (index)
- variable
- value (if different valuetypes cast to string)

#### Wideformat

columns:

- datetime or timestamp (index)
- columns for each variable (with valuetype)

### Csv
