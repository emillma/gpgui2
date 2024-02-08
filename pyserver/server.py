import asyncio
from websockets import serve, WebSocketServerProtocol
from urllib import parse


async def hello(websocket: WebSocketServerProtocol, path):
    try:
        print(websocket, path)
        while True:
            await websocket.send("Hello, world!")
            await asyncio.sleep(1)
    except Exception as e:
        print(e)


async def main():
    async with serve(hello, "127.0.0.1", 12102):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
