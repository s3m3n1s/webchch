from typing import NamedTuple

from database.targets.targets_worker import FileWorker


class UtilsNames(NamedTuple):
    Util1 = "Wad"
    Util2 = "WhatWeb"
    Util0 = "Custom"


async def console_controller_loop():
    await FileWorker.init()

    while True:
        print("\n__________________________________"
              "\nChoose what you want:")
        print("1. Add url\n2. Delete url\n")
        what_to_do = int(input("Write task number: "))

        if what_to_do == 1:
            url = str(input("Input target url: "))
            frequency = int(input("Input frequency of checking url (in seconds): "))
            scan_util_n = int(input(f"Input № of util to scan url:"
                                    f"\n\t1. {UtilsNames.Util1}"
                                    f"\n\t2. {UtilsNames.Util2}"
                                    f"\n"))

            if scan_util_n == 1:
                scan_util = "Wad"
            elif scan_util_n == 2:
                scan_util = "WhatWeb"
            else:
                scan_util = "Custom"

            url_info = {"frequency": frequency, "scan_util": scan_util}
            target = {url: url_info}

            await FileWorker.append_value(file_name=FileWorker.file_with_curr_targets, value=target, key="curr_targets")
            await FileWorker.append_value(file_name=FileWorker.file_with_all_targets, value=target, key="all_targets")
        elif what_to_do == 2:
            print("Input urls for stop scanning: ", end="")
            url = input()
            target = {url: ""}
            await FileWorker.append_value(file_name=FileWorker.file_with_stop_targets,
                                          value=target, key="stop_targets")
        else:
            print("Select correct number.")
