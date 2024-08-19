import json

import pandas as pd


def df_description_str(df: pd.DataFrame) -> str:
    number_of_coluumns = len(df.columns)
    df_describe_str = df.describe(include="all").T.to_string()
    df_describe_str = "  " + df_describe_str.replace("\n", "\n  ")
    df_types_str = df.dtypes.to_string()
    df_types_str = "  " + df_types_str.replace("\n", "\n  ")

    string: str = ""
    string += "Dataframe:"
    string += f"\n Shape: {df.shape}"

    string += f"\n Columns [{number_of_coluumns}]: {df.columns}"
    string += f"\n Rows [{len(df.index)}]: {df.index}"

    string += f"\n Count NaN:\n{df.isna().sum()}"

    string += f"\n Describe:\n{df_describe_str}"
    string += f"\n dtpes:\n{df_types_str}"

    return string


def df_description_json(df: pd.DataFrame) -> dict:
    df_describe_json = dict(json.loads(df.describe().to_json()))
    return df_describe_json


def df_description_markdown(df: pd.DataFrame) -> str:
    # TODO: dependency tabulate
    df_describe_markdown = df.describe().T.to_markdown()

    return df_describe_markdown
