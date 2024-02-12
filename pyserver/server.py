import asyncio

# from asyncio import
from asyncio.subprocess import PIPE, create_subprocess_shell, Process
from websockets import serve, WebSocketServerProtocol
import json
from pathlib import Path
import itertools


class Terminal:
    def __init__(self):
        self.messages = []

        self.running = False
        self.proc: Process | None = None

        self.reader_task = None
        self.message_event = asyncio.Event()

    async def start(self, cmd):
        assert not self.running
        self.running = True
        self.proc = await create_subprocess_shell(cmd, stdout=PIPE, stderr=PIPE)

        async def read_task():
            async for message in self.proc.stdout:
                self.messages.append(message)
                self.message_event.set()

        self.reader_task = asyncio.create_task(read_task())

    async def stop(self):
        self.proc.terminate()
        await self.proc.wait()
        self.running = False

    async def message_iter(self):
        for i in itertools.count():
            while i >= len(self.messages):
                await self.message_event.wait()
                self.message_event.clear()
            yield self.messages[i]


terminals: dict[str, Terminal] = {}


async def run_cmd(cmd: str, sock: WebSocketServerProtocol):
    if (term := terminals.get(cmd, None)) is None:
        term = terminals[cmd] = Terminal()

    async def sock_reader():
        async for data in sock:
            if data == "start":
                import random

                msg = f"Printing something every second {random.random()}"
                await term.start(f'while true; do echo "{msg}"; sleep 1; done')
            elif data == "stop":
                await term.stop()
            else:
                raise ValueError(f"unexpected message: {data}")

    async def process_reader():
        async for data in term.message_iter():
            await sock.send(json.dumps(dict(type="message", data=data.decode())))

    async def status_sender():
        while True:
            await sock.send(json.dumps(dict(type="status", data=str(term.running))))
            await asyncio.sleep(0.2)

    await asyncio.gather(sock_reader(), process_reader(), status_sender())


async def handle(sock: WebSocketServerProtocol, path):

    if path == "/video":
        while True:
            data = Path("/workspaces/gui/pyserver/jpeg420exif.jpg").read_bytes()
            await sock.send(data)
            await asyncio.sleep(0.2)
            data = Path("/workspaces/gui/pyserver/jpeg444.jpg").read_bytes()
            await sock.send(data)
            await asyncio.sleep(0.2)

    if path == "/run_ls":
        await run_cmd("ls", sock)


async def main():
    async with serve(handle, "127.0.0.1", 12102):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
