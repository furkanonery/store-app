import os
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = 'redis://'+os.getenv("REDIS_URL")