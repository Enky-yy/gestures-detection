from fastapi import FastAPI, WebSocket
from backend.vision.gesture_pipeline import GesturePipeline
from backend.events.gesture_events import send_gesture

app = FastAPI()

pipeline = GesturePipeline()

@app.websocket("/ws")

async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()

    while True:

        gesture = pipeline.process()

        if gesture:
            await send_gesture(websocket, gesture)