import asyncio
from websockets.server import serve
from websockets import WebSocketServerProtocol


async def echo(websocket: WebSocketServerProtocol, path: str):
    for i in range(10000):
        await websocket.send(f"{i}")
        await asyncio.sleep(1)


async def main():
    async with serve(echo, "localhost", 8888):
        await asyncio.Future()  # run forever


asyncio.run(main())
