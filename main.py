from fastapi import FastAPI
from routes.lampada import rota_lampada

app = FastAPI()

app.include_router(rota_lampada)