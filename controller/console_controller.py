import asyncio

from database.targets.targets_worker import FileWorker
import database.targets.targets_worker as targets_worker


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
            target = {url: frequency}
            # target = {"url": url, "frequency": frequency}

            await FileWorker.append_value(file_name=FileWorker.file_with_curr_targets, value=target, key="curr_targets")
            await FileWorker.append_value(file_name=FileWorker.file_with_all_targets, value=target, key="all_targets")
        elif what_to_do == 2:
            print("Input urls for stop scanning: ", end="")
            url = int(input())
            target = {url: ""}
            await FileWorker.append_value(file_name=FileWorker.file_with_stop_targets,
                                          value=target, key="stop_targets")
        else:
            print("Select correct number.")
