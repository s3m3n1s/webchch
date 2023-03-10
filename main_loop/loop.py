import asyncio
from asyncio import sleep, create_task

import database.targets.targets_worker as targets_worker
from analyzer.analyzer_factory import Analyzer

from configuration.config import TIME_UPD_TASK_QUEUE


asyncio.run(targets_worker.create_target_queue())


async def period_analyzing(freq: int, url: str, scan_util: str):
    while True:
        stop_list = await targets_worker.get_stop_urls(key="stop_targets")
        if url in stop_list["stop_targets"].keys():
            await targets_worker.del_url(url)
            print(f">> Target with url '{url}' deleted from tasks queue")
            break
        analyzer = Analyzer(analyze_util=scan_util)
        analyzer.analyze(url=url)
        print(f">> Util '{scan_util}' working with url: {url}")
        if analyzer.difference != "None":
            print(">> difference:\n", analyzer.difference)
        await sleep(freq)


async def loop():
    while True:
        target_to_check = await targets_worker.get_curr_targets(key="curr_targets")

        for target in target_to_check["curr_targets"].items():
            url, url_info = target
            frequency = url_info["frequency"]
            scan_util = url_info["scan_util"]
            create_task(period_analyzing(freq=frequency, url=url, scan_util=scan_util))

        await sleep(TIME_UPD_TASK_QUEUE)
