from typing import NamedTuple

from database.targets.targets_worker import FileWorker

import argparse


class UtilsNames(NamedTuple):
    Util1 = "Wad"
    Util2 = "WhatWeb"
    Util0 = "Custom"


async def console_controller():
    await FileWorker.init()

    parser = argparse.ArgumentParser(
        description="WebChangeChecker - utility for observe website and track important change")
    parser.add_argument("url", type=str, help="url address to check changes")
    parser.add_argument("-f", "--freq", metavar="frequency", type=int, default=3600,
                        help="url address check frequency in seconds (default: 3600)")
    parser.add_argument("-su", "--scan_util", metavar="scan_util", type=str, default="Wad",
                        help="input № of util to scan url: {:s}, {:s} (default: Wad)".format(UtilsNames.Util1,
                                                                                             UtilsNames.Util2))
    parser.add_argument("-d", "--delete", action="store_true", help="flag to remove url from check changes list")
    args = parser.parse_args()

    if not args.delete:
        url = args.url
        frequency = args.freq
        scan_util_n = args.scan_util

        if scan_util_n != "Wad" and scan_util_n != "WhatWeb":
            print("Argument -su / --scan_util entered incorrectly. Please use 'Wad' or 'WhatWeb'")
            return
        else:
            scan_util = scan_util_n

        url_info = {"frequency": frequency, "scan_util": scan_util}
        target = {url: url_info}

        await FileWorker.append_value(file_name=FileWorker.file_with_curr_targets, value=target, key="curr_targets")
        await FileWorker.append_value(file_name=FileWorker.file_with_all_targets, value=target, key="all_targets")

        print("Added {:s} to targets with frequency {:d} seconds and scan util {:s}".format(url, frequency, scan_util))

    elif args.delete:
        url = args.url
        target = {url: ""}
        await FileWorker.append_value(file_name=FileWorker.file_with_stop_targets,
                                      value=target, key="stop_targets")

        print("Deleted {:s} from targets".format(url))
