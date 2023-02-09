from asyncio import sleep, create_task

import database.targets.targets_worker as targets_worker
from configuration.config import TIME_UPD_TASK_QUEUE


targets_worker.create_target_queue()


async def period_analyzing(freq: int, url: str):
    while True:
        if url in await targets_worker.get_stop_urls():
            await targets_worker.del_stop_url(url)
            await targets_worker.del_url_from_all_targets(url)
            print(f">> Target with url {url} deleted")
            break
        # analyzer = Analyzer(url=url)
        # result = analyzer.analyze_by_url()
        # print(result)
        print(f">>working url: {url}")
        await sleep(freq)


async def loop():
    while True:
        target_to_check = await targets_worker.get_curr_targets()
        await targets_worker.clear_curr_targets()

        for target in target_to_check:
            url = target["url"]
            frequency = target["frequency"]

            create_task(period_analyzing(freq=frequency, url=url))

        await sleep(TIME_UPD_TASK_QUEUE)
