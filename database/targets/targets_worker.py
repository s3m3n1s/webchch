import json

from typing import NamedTuple

import database.targets.config as config


file_with_all_targets = config.file_with_all_targets
file_with_curr_targets = config.file_with_curr_targets
file_with_stop_targets = config.file_with_stop_targets


class FileWorker:
    file_with_all_targets = config.file_with_all_targets
    file_with_curr_targets = config.file_with_curr_targets
    file_with_stop_targets = config.file_with_stop_targets

    @staticmethod
    async def init():
        await FileWorker.__create_file_if_not_exist(file_name=file_with_all_targets, default_data_type="json", key="all_targets")
        await FileWorker.__create_file_if_not_exist(file_name=file_with_curr_targets, default_data_type="json", key="curr_targets")
        await FileWorker.__create_file_if_not_exist(file_name=file_with_stop_targets, default_data_type="json", key="stop_targets")

    @staticmethod
    async def __create_file_if_not_exist(file_name: str, default_data_type: str, key: str):
        data = {}
        if default_data_type == "json":
            data = {key: {}}
        elif default_data_type == "list":
            data = []
        elif default_data_type == "str":
            data = ""

        try:
            with open(file_name, "r") as f:
                f.read()
        except:
            with open(file_name, "w") as f:
                json.dump(data, f)

    @staticmethod
    async def read_json(file_name: str, key: str) -> json:
        data = {key: {}}
        try:
            with open(file_name, "r") as f:
                data = json.load(f)
        except Exception as E:
            print("read_json >>>> ", E)
        return data

    @staticmethod
    async def write_json(file_name: str, json_data: json):
        with open(file_name, "w") as f:
            json.dump(json_data, f)

    @staticmethod
    async def append_value(file_name: str, value: json, key: str):
        cur_data = await FileWorker.read_json(file_name=file_name, key=key)

        cur_data[key] = {**cur_data[key], **value}

        await FileWorker.write_json(file_name=file_name, json_data=cur_data)

    @staticmethod
    async def remove_value(file_name: str, value: str, key: str):
        cur_data = await FileWorker.read_json(file_name=file_name, key=key)
        del cur_data[key][str(value)]

        await FileWorker.write_json(file_name=file_name, json_data=cur_data)

    @staticmethod
    async def clear_targets(file_name: str, key: str):
        with open(file_name, "w") as f:
            json.dump({key: {}}, f)


async def create_target_queue():
    """
    used every start of program
    """
    data = {}
    targets = await FileWorker.read_json(file_with_all_targets, key="all_targets")
    data["curr_targets"] = targets["all_targets"]
    await FileWorker.write_json(file_name=file_with_curr_targets, json_data=data)


async def get_curr_targets(key: str) -> dict:
    targets = await FileWorker.read_json(file_with_curr_targets, key)
    await FileWorker.clear_targets(file_with_curr_targets, key=key)

    return targets


async def get_stop_urls(key):
    stop_url_list = await FileWorker.read_json(file_with_stop_targets, key)
    return stop_url_list


async def del_url_from_all_targets(url: str):
    all_targets = await FileWorker.read_json(file_with_all_targets, "all_targets")
    del all_targets["all_targets"][url]
    await FileWorker.write_json(file_with_all_targets, all_targets)


async def del_url(url: str):
    await FileWorker.remove_value(file_name=file_with_stop_targets, value=url, key="stop_targets")
    await del_url_from_all_targets(url)
