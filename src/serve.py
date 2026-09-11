import asyncio
from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosedOK
import json


async def handler(websocket):
    async for data in websocket:
        data = json.loads(data)
        print(data)
        if (("message" in data) & (data["message"] == "hello")):
            await websocket.send(json.dumps({"message": "hello"}))

async def main():
    print("Starting websocket server...")
    server = await serve(handler, "", 8001)
    print("Awaiting connection")
    await server.serve_forever()

asyncio.run(main())