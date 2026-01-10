import os
from dotenv import load_dotenv
from pydantic.v1 import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    OPENAI_API_KEY = "" # os.getenv('WHATSAPP_TOKEN')
    WHATSAPP_TOKEN = "" # os.getenv('WHATSAPP_PHONE_ID')
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')
