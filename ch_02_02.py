import asyncio
import click

import websockets


def render_message(message: str) -> str:
    click.clear()
    if "BLASTOFF" in message:
        click.secho(message, blink=True, bold=True, fg="red")
    else:
        click.secho(message, bold=True, fg="green")


async def chat() -> None:
    uri = "ws://localhost:8000"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello world!")
        async for message in websocket:
            render_message(message)
            if "BLASTOFF" in message:
                break


async def main() -> None:
    await asyncio.gather(chat())


if __name__ == "__main__":
    asyncio.run(main())
