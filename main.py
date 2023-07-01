import asyncio


async def wait(delay, message):
    await asyncio.sleep(delay)
    print(message)


async def main():
    arr_awaits = [[5, "One"], [1, "Two"], [3, "Three"], [2, "Four"], [4, "Five"]]

    def_await = []

    for await_ in arr_awaits:
        def_await.append(asyncio.create_task(wait(await_[0], await_[1])))

    for await_ in def_await:
        await await_


asyncio.run(main())
