from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from utils import lampada
from schemas.modo import Modo

rota_lampada = APIRouter(prefix='/v1')
templates = Jinja2Templates(directory="templates")

@rota_lampada.get('/status')
def status():

    lamp = lampada()
    
    return lamp.status()

@rota_lampada.post("/on")
def turn_on():
    lamp = lampada()
    lamp.turn_on()
    return {"status": "on"}

@rota_lampada.post("/off")
def turn_off():
    lamp = lampada()
    lamp.turn_off()
    return {"status": "off"}

@rota_lampada.post("/brightness/{value}")
def set_brightness(value: int):
    lamp = lampada()
    value = max(1, min(value, 100))
    lamp.set_brightness_percentage(value)
    return {"brightness": value}

@rota_lampada.post("/color/{r}/{g}/{b}")
def set_color(r: int, g: int, b: int):
    lamp = lampada()
    lamp.set_colour(r, g, b)
    return {"color": [r, g, b]}

@rota_lampada.post("/mode/{modo}")
def white(modo:Modo):
   lamp = lampada()
   lamp.set_mode(modo) 

@rota_lampada.get("/",response_class=HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse(request,"index.html")