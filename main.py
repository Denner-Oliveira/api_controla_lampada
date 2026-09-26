import tinytuya
import os
from dotenv import load_dotenv

load_dotenv()

DEVICE_ID = os.getenv("DEVICE_ID")
IP = os.getenv("IP")
LOCAL_KEY = os.getenv("LOCAL_KEY")

lamp = tinytuya.BulbDevice(DEVICE_ID, IP, LOCAL_KEY)
lamp.set_version(3.5)

print(lamp.status())
lamp.turn_on()
lamp.set_brightness_percentage(255)
lamp.set_colour(255, 255, 255)
lamp.set_white(colourtemp=10)