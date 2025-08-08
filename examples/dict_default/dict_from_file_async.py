import asyncio
from pathlib import Path
from pprint import pprint

from atptools import DictDefault


async def main() -> None:
    def_dict = DictDefault()
    # await def_dict.from_json_async(Path("data_sample", "dict_test", "test1.json"))
    # await def_dict.from_yaml_async(Path("data_sample", "dict_test", "test1.yaml"))
    # await def_dict.from_toml_async(Path("data_sample", "dict_test", "test1.toml"))
    await def_dict.from_file_async(Path("data_sample", "dict_test", "test1.json"))
    # await def_dict.from_file_async(Path("data_sample", "dict_test", "test1.yaml"))
    # await def_dict.from_file_async(Path("data_sample", "dict_test", "test1.yml"))
    # await def_dict.from_file_async(Path("data_sample", "dict_test", "test1.toml"))

    print("def_dict")
    pprint(def_dict)

    return None


if __name__ == "__main__":
    asyncio.run(main())
