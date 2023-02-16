import asyncio

from main_loop.loop import loop


if __name__ == "__main__":
    print("App is running")
    asyncio.run(loop())
