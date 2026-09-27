import tinytuya
import os
from dotenv import load_dotenv

def lampada():
    load_dotenv()

    DEVICE_ID = os.getenv("DEVICE_ID")
    IP = os.getenv("IP")
    LOCAL_KEY = os.getenv("LOCAL_KEY")

    lamp = tinytuya.BulbDevice(DEVICE_ID, IP, LOCAL_KEY)
    lamp.set_version(3.5)

    return lamp