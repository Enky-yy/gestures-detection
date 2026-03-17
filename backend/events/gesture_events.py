import json

async def send_gesture(websocket, gesture):

    message = json.dumps({
        "gesture": gesture
    })

    await websocket.send_text(message)