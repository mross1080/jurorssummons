#!/usr/bin/env python

# WS client example

import asyncio
import websockets

async def processMessage():
    uri = "ws://localhost:8080"
    while True:
        async with websockets.connect(uri) as websocket:
            print("Got a new message from server")
            name = "Jerb"

            await websocket.send(name)
            print(f"> {name}")

            greeting = await websocket.recv()
            print(f"< {greeting}")
loop = asyncio.get_event_loop()

loop.run_until_complete(processMessage())
loop.run_forever()
