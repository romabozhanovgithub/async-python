import asyncio
import time
from datetime import datetime

import click


# SYNC
def sleep_and_print(sleep_time: int) -> int:
    print(f"Sleeping for {sleep_time} seconds")
    time.sleep(sleep_time)
    print(f"Finished sleeping for {sleep_time} seconds")
    return sleep_time


start = datetime.now()
print([sleep_and_print(5), sleep_and_print(8)])
end = datetime.now()
click.secho(f"Total time taken: {end - start}", fg="green")


# ASYNC
async def sleep_and_print_async(sleep_time: int) -> int:
    print(f"Sleeping for {sleep_time} seconds")
    await asyncio.sleep(sleep_time)
    print(f"Finished sleeping for {sleep_time} seconds")
    return sleep_time


async def main():
    # Using arguments
    start = datetime.now()
    await asyncio.gather(sleep_and_print_async(5), sleep_and_print_async(8))
    end = datetime.now()
    click.secho(f"Total time taken: {end - start}", fg="green")

    # Building a list of coroutines
    # start = datetime.now()
    # coroutines = [sleep_and_print_async(5), sleep_and_print_async(8)]
    # await asyncio.gather(*coroutines)
    # end = datetime.now()
    # click.secho(f"Total time taken: {end - start}", fg="green")


asyncio.run(main())
