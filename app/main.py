from fastapi import FastAPI, WebSocketDisconnect
from typing import List


app = FastAPI()


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebDocket] = []
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
    
    def disconnect(self, websocket)