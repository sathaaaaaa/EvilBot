#Kiitu
import asyncio
import sys

from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from EvilBot import MONGO_DB_URI 
from EvilBot.conf import get_int_key, get_str_key



MONGO_PORT = get_int_key("27017")
MONGO_DB_URI = get_str_key("MONGO_DB_URI")
MONGO_DB = "Evil"


client = MongoClient()
client = MongoClient(MONGO_DB_URI, MONGO_PORT)[MONGO_DB]
db = motor[MONGO_DB]
db = client["evilbot"]
try:
    asyncio.get_event_loop().run_until_complete(motor.server_info())
except ServerSelectionTimeoutError:
    sys.exit(log.critical("Can't connect to mongodb! Exiting..."))
