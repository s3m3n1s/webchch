import asyncio
from asyncio import sleep, create_task

import database.targets.targets_worker as targets_worker
from database.targets.targets_worker import FileWorker
from configuration.config import TIME_UPD_TASK_QUEUE


asyncio.run(targets_worker.create_target_queue())


async def period_analyzing(freq: int, url: str):
    while True:
        stop_list = await targets_worker.get_stop_urls(key="stop_targets")
        if url in stop_list["stop_targets"].keys():
            await targets_worker.del_url(url)
            print(f">> Target with url '{url}' deleted")
            break
        # analyzer = Analyzer(url=url)
        # result = analyzer.analyze_by_url()
        # print(result)
        print(f">> Working with url: {url}")
        await sleep(freq)


async def loop():
    while True:
        target_to_check = await targets_worker.get_curr_targets(key="curr_targets")

        for target in target_to_check["curr_targets"].items():
            url, frequency = target
            create_task(period_analyzing(freq=frequency, url=url))

        await sleep(TIME_UPD_TASK_QUEUE)
