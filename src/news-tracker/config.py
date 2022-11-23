import os

from dotenv import load_dotenv

load_dotenv()

RAPID_API_KEY = os.getenv('RAPID_API_KEY')
API_URI = os.getenv('API_URI')
DB_URL = os.getenv('DB_URL')
SECRET_KEY = os.getenv('SECRET_KEY')