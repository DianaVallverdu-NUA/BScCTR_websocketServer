import asyncio
from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosedOK
import json


async def handler(websocket):
    while True:
        try:
            data = await websocket.recv()
            data = json.loads(data)
        except ConnectionClosedOK:
            print("connection has closed. Awaiting new connection...")
            break
        if (("message" in data) & (data["message"] == "hello")):
            await websocket.send(json.dumps({"message": "hello"}))

async def main():
    print("Starting websocket server...")
    server = await serve(handler, "", 8001)
    print("Awaiting connection")
    await server.serve_forever()

asyncio.run(main())