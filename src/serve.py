import asyncio
from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosedOK
import json

CLIENTS = set()

async def broadcastMessage(data):
    message = ""
    if("name" in data) :
        message = data["name"] + ": "
    else :
        message = "Anonymous User: "
    message = message + data["message"]
    response = {"message": message}
    for websocket in CLIENTS.copy():
        try:
            await websocket.send(json.dumps(response))
        except ConnectionClosedOK:
            pass

async def handler(websocket):
    CLIENTS.add(websocket)
    async for data in websocket:
        data = json.loads(data)
        
        if("message" in data) :
            await broadcastMessage(data)
            continue
        
        if("name" in data) :
            await websocket.send(json.dumps({"message": "welcome to the chat, " + data["name"]}))

async def main():
    print("Starting websocket server...")
    server = await serve(handler, "", 8001)
    print("Awaiting connection")
    await server.serve_forever()

asyncio.run(main())