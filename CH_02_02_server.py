import asyncio
import websockets
import click
from contextlib import suppress


async def blastoff(websocket):
    click.secho(">>  begin blastoff")
    for i in range(25):
        await websocket.send(f"\n\n\n>> {'  ' * i}🚀")
        await asyncio.sleep(0.03)
    for i in range(3):
        await asyncio.sleep(0.5)
        await websocket.send(f"\n\n\n>>   🚀🚀🚀🚀🚀🚀🚀🚀 BLASTOFF 🚀🚀🚀🚀🚀🚀🚀🚀  <<")


async def huston(websocket):
    click.clear()
    async for message in websocket:
        if "yes" in message.lower():
            click.secho(">> begin countdown")
            for i in reversed(range(1, 11)):
                await websocket.send(f"\n\n\n>>   Taking off in: {i}")
                await asyncio.sleep(0.8)
        with suppress(Exception):
            await blastoff(websocket)


async def main():
    PORT = 8765
    click.secho(f"--- listening for websocket connections on port: {PORT} ---")
    async with websockets.serve(huston, "fatima.robertimpey.com", PORT):
        await asyncio.Future()


asyncio.run(main())
