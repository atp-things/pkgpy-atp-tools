import json
from collections import defaultdict
from pathlib import Path


class Dict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_json(self, path: str | Path | None = None):
        ret = json.dumps(
            self,
            default=str,
            ensure_ascii=False,
        )
        if path is not None:
            path = _path_suffix_check(path, suffix=".json")
            _save_string_to_file(ret, path)
        return ret


class DictDefault(defaultdict):
    def __init__(self, *args, **kwargs):
        super().__init__(dict, *args, **kwargs)

    def to_json(self, path: str | Path | None = None):
        ret = json.dumps(
            self,
            default=str,
            ensure_ascii=False,
        )
        if path is not None:
            path = _path_suffix_check(path, suffix=".json")
            _save_string_to_file(ret, path)
        return ret


def _save_string_to_file(string: str, path: str | Path) -> None:
    with open(path, "w", encoding="utf-8") as file:
        file.write(string)

    return


def _path_suffix_check(path: Path | str, suffix: str) -> Path:
    if isinstance(path, str):
        path = Path(path)

    if path.suffix != suffix:
        path = path.with_suffix(suffix)
    return path
