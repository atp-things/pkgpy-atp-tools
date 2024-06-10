import json
from collections import UserList, defaultdict
from pathlib import Path

from .utils import _path_suffix_check, _save_string_to_file


class Records(list[dict]):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_list(self) -> list:
        return list(self)

    def to_json(
        self,
        path: str | Path | None = None,
        indent: int | None = None,
    ) -> str:
        ret = json.dumps(
            list(self),
            default=str,
            ensure_ascii=False,
            indent=indent,
        )
        if path is not None:
            path = _path_suffix_check(path, suffix=".json")
            _save_string_to_file(ret, path)
        return ret

    def from_json(self, path: str | Path):
        with open(path, encoding="utf-8") as file:
            super().extend(json.load(file))
        return self

    def to_dict(self, keys: list) -> defaultdict:
        ret: defaultdict = defaultdict(dict)
        for record in self:
            key_values = [record[key] for key in keys]
            ret_local = record
            for key in key_values[::-1]:
                ret_local = {key: ret_local}
            ret.update(ret_local)

        return ret
