import asyncio
from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosedOK


async def handler(websocket):
    while True:
        try:
            message = await websocket.recv()
        except ConnectionClosedOK:
            print("connection has closed. Awaiting new connection...")
            break
        print(message)

async def main():
    print("Starting websocket server...")
    server = await serve(handler, "", 8001)
    print("Awaiting connection")
    await server.serve_forever()

asyncio.run(main())