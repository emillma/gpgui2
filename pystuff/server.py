
import asyncio
from websockets import serve, WebSocketServerProtocol

async def echo(websocket: WebSocketServerProtocol, path: str) -> None:
    print("Connected")
    # async for message in websocket:
    #     await websocket.send(message)

async def main():
    async with serve(echo, "localhost", 12102):
        await asyncio.Future()  # run forever

asyncio.run(main())