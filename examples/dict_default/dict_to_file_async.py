import asyncio
from pathlib import Path
from pprint import pprint

from atptools import DictDefault


# DictDefault---------------------------------------------------------------
async def main() -> None:
    dict_default = DictDefault()
    await dict_default.from_json_async(Path("data_sample", "dict_test", "test1.json"))
    await dict_default.to_json_async(
        Path("data", "output", "dict_default_test1.json"), indent=2
    )
    await dict_default.to_yaml_async(Path("data", "output", "dict_default_test1.yaml"))
    await dict_default.to_toml_async(Path("data", "output", "dict_default_test1.toml"))
    print("def_dict")
    pprint(dict_default)

    return None


if __name__ == "__main__":
    asyncio.run(main())
