import json

import database.targets.config as config


file_with_all_targets = config.file_with_all_targets
file_with_curr_targets = config.file_with_curr_targets
file_with_stop_targets = config.file_with_stop_targets


def create_target_queue():
    """
    used every start of program
    """
    try:
        with open(file_with_all_targets, "r") as f:
            targets_to_check = json.load(f)
        with open(file_with_curr_targets, "w") as f:
            json.dump(targets_to_check, f)
    except:
        pass


async def get_curr_targets() -> list:
    target_to_check = []
    try:
        with open(file_with_curr_targets, "r") as f:
            target_to_check = json.load(f)
    except:
        pass
    # target_to_check = [{"url": "1", "frequency": 3}, {"url": "2", "frequency": 3}, {"url": "3", "frequency": 3}]
    return target_to_check


async def get_stop_urls() -> list:
    stop_url_list = []
    try:
        with open(file_with_stop_targets, "r") as f:
            stop_url_list = json.load(f)
    except:
        pass
    # stop_url_list = ["1", "2"]
    return stop_url_list


async def del_stop_url(url: str):
    try:
        with open(file_with_stop_targets, "r") as f:
            targets_to_stop = json.load(f)

        targets_to_stop.pop(targets_to_stop.index(url))
        with open(file_with_stop_targets, "w") as f:
            json.dump(targets_to_stop, f)
    except:
        pass


async def del_url_from_all_targets(url: str):
    try:
        with open(file_with_all_targets, "r") as f:
            all_targets = json.load(f)

        for _, target in enumerate(all_targets):
            if target["url"] == url:
                all_targets.pop(_)

        with open(file_with_all_targets, "w") as f:
            json.dump(all_targets, f)
    except Exception as E:
        print(E)


async def clear_curr_targets():
    try:
        with open(file_with_curr_targets, "w") as f:
            json.dump({}, f)
    except:
        pass
