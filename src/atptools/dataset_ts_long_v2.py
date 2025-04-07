import datetime as dt
import uuid
from typing import Any

import pandas as pd

from .dataframe import df_description_str
from .dict_default import DictDefault
from .records import Records


class AtpDatasetTsLongV2:
    def __init__(
        self,
        # column_name_index: list[str] | None = None,
        columns: dict[str, Any] | None = None,
    ):
        self._init_columns(columns=columns)
        self._init_dataframe()

        return

    def _init_columns(self, columns: dict[str, Any] | None) -> None:
        self.column_all = ["dt", "value"]
        self.column_index = ["dt"]
        self.column_other = []
        self.df_empty_data = {
            "dt": pd.Series(dtype="datetime64[ns]"),
            "value": pd.Series(dtype="float"),
        }
        if columns is not None:
            for key, value in columns.items():
                self.column_all += [key]

                if value.get("index", False):
                    self.column_index += [key]
                else:
                    self.column_other += [key]
                self.df_empty_data[key] = pd.Series(dtype=value.get("type", "str"))
        print("self.column_all:", self.column_all)
        return None

    def _init_dataframe(
        self,
    ) -> "AtpDatasetTsLongV2":
        self.df: pd.DataFrame = pd.DataFrame(self.df_empty_data)
        self.df.set_index(self.column_index, inplace=True)
        return self

    def add_dataframe(self, df: pd.DataFrame) -> "AtpDatasetTsLongV2":
        df_local = df.copy()
        # TODO: cast columns to the correct type
        df_local.reset_index(drop=True, inplace=True)
        df_local.set_index(self.column_index, inplace=True)
        self.df = pd.concat(
            [self.df, df_local],
            axis="index",
            # ignore_index=True,
        )
        self.df = self.df[~self.df.index.duplicated(keep="last")]
        print("self.df:", self.df)
        # self.df.set_index(self.column_index, inplace=True)
        return self

    def to_dataframe(self) -> pd.DataFrame:
        return self.df

    def empty_data(self) -> "AtpDatasetTsLongV2":
        del self.df
        self._init_dataframe()
        return self

    def get_time_range(self) -> tuple[dt.datetime, dt.datetime]:
        return self.df.index.min(), self.df.index.max()

    def get_dataframe_description(self) -> str:
        return df_description_str(self.df)
