#ACM
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "25058583"))
API_HASH = environ.get("API_HASH", "8caa296e93bfd29cacd9d83b242979cc")
BOT_TOKEN = environ.get("BOT_TOKEN", "8058389557:AAFt4Zrto_VaL1SUBbpCwLkGyImJA-pREkg")

OWNER = int(environ.get("OWNER", "7648522061"))
CREDIT = environ.get("CREDIT", "𝐒ɑη𝐣ɑʏ")

TOTAL_USER = os.environ.get('TOTAL_USERS', '7648522061').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '7648522061').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set





