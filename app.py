import asyncio

from main_loop.loop import loop


if __name__ == "__main__":
    asyncio.run(loop())


# {"url": "0", "frequency": 3}, {"url": "1", "frequency": 3},{"url": "2", "frequency": 3}, {"url": "3", "frequency": 3}
