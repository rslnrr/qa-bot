import os
import sys
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    print("ERROR: BOT_TOKEN is not set. Check your .env file.")
    sys.exit(1)

QUIZ_SIZE = 10
