import asyncio
import aiohttp
from datetime import datetime
from pprint import pprint

import click
import requests


urls = [
    "http://httpbin.org/get?text=python",
    "http://httpbin.org/get?text=is",
    "http://httpbin.org/get?text=fun",
    "http://httpbin.org/get?text=and",
    "http://httpbin.org/get?text=useful",
]


# SYNC
def fetch(url: str) -> dict:
    response = requests.get(url)
    return response.json()["args"]


start = datetime.now()
pprint([fetch(url) for url in urls])
end = datetime.now()
click.secho(f"Time taken: {end - start}", fg="green")


# ASYNC
async def fetch_url(session: aiohttp.ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        response = await response.json()
        return response["args"]

async def fetch_async() -> list:
    async with aiohttp.ClientSession() as session:
        cors = []
        for url in urls:
            cors.append(fetch_url(session, url))
        return await asyncio.gather(*cors)
    

start = datetime.now()
pprint(asyncio.run(fetch_async()))
end = datetime.now()
click.secho(f"Time taken: {end - start}", fg="green")
