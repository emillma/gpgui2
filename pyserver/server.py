import asyncio
from asyncio.subprocess import PIPE, create_subprocess_shell, Process
from websockets import serve, WebSocketServerProtocol
import json


scripts: dict[str, Process] = dict()


async def run_cmd(cmd: str, socket: WebSocketServerProtocol):
    if proc := scripts.get(cmd, None) is None:
        scripts[cmd] = await create_subprocess_shell(cmd, stdout=PIPE, stderr=PIPE)
        proc = scripts[cmd]

    async def sock_reader():
        async for data in socket:
            if data == "STOP":
                proc.terminate()
                break

    async def process_reader():
        async for data in proc.stdout:
            await socket.send(data.decode())

    await socket.send("\nDONE\n\n")


async def handle(sock: WebSocketServerProtocol, path):
    if path == "/run_ls":
        await run_cmd("ls", sock)


async def main():
    async with serve(handle, "127.0.0.1", 12102):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
