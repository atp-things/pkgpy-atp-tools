import json
from collections import defaultdict
from pathlib import Path

import toml
import yaml

from .io import save_to_file
from .utils import _path_suffix_check


class DictDefault(defaultdict):
    def __init__(self, *args, **kwargs):
        super().__init__(dict, *args, **kwargs)

    def to_dict(self) -> dict:
        return dict(self)

    def to_defaultdict(self) -> dict:
        return defaultdict(dict, self)

    def from_dict(self, dict_: defaultdict | dict):
        super().update(dict_)
        return self

    def to_json(
        self,
        path: str | Path | None = None,
        indent: int | None = None,
    ) -> str:
        ret = json.dumps(
            dict(self),
            default=str,
            ensure_ascii=False,
            indent=indent,
        )
        if path is not None:
            path = _path_suffix_check(path, suffix=".json")
            save_to_file(ret, path)
        return ret

    def to_yaml(
        self,
        path: str | Path | None = None,
        indent: int | None = None,
    ) -> str:
        ret = yaml.dump(
            dict(self),
            default_flow_style=False,
            allow_unicode=True,
            indent=indent,
        )
        if path is not None:
            save_to_file(ret, path)
        return ret

    def to_toml(self, path: str | Path | None = None) -> str:
        ret = toml.dumps(dict(self))
        if path is not None:
            save_to_file(ret, path)
        return ret

    def from_file(self, path: str | Path):
        if isinstance(path, str):
            path = Path(path)

        suffix = path.suffix
        match suffix:
            case ".json":
                self.from_json(path)
            case ".yaml" | ".yml":
                self.from_yaml(path)
            case ".toml":
                self.from_toml(path)
            case _:
                raise ValueError("Invalid file format")

        return self

    def from_json(self, path: str | Path):
        with open(path, encoding="utf-8") as file:
            super().update(json.load(file))
        return self

    def from_yaml(self, path: str | Path):
        with open(path, encoding="utf-8") as file:
            super().update(yaml.safe_load(file))
        return self

    def from_toml(self, path: str | Path):
        with open(path, encoding="utf-8") as file:
            super().update(toml.load(file))
        return self

    def rename_keys(self, rename_dict: dict) -> dict:
        # TODO: #14 add support for nested keys
        for key, value in rename_dict.items():
            if key in self:
                self[value] = self.pop(key)
        return self

    def to_vector(
        self,
        keys: list | None = None,
        flatten: bool = False,
    ) -> list | tuple[list, list]:
        """Converts the dictionary to a vector

        Parameters
        ----------
        keys : list | None, optional
            Keys to be converted into vector, by default None
        flatten : bool, optional
            Flatten lists, by default False

        Returns
        -------
        list | tuple[list, list]
            if keys is None, returns a tuple of keys and values
            if keys is not None, returns a list of values
        """
        if keys is None:
            return list(self.keys()), list(self.values())

        values = []

        for key in keys:
            # if key is a list, then it is a nested key
            if isinstance(key, list):
                subvalue = self[key[0]]
                for k in key[1:]:
                    subvalue = subvalue[k]
                values.append(subvalue)
            else:
                values.append(self[key])

        if flatten:
            # flatten only one level
            values_new = []
            for value in values:
                if isinstance(value, list):
                    values_new.extend(value)
                else:
                    values_new.append(value)

            values = values_new

        return values
