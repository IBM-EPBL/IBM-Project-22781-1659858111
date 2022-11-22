import os

from dotenv import load_dotenv

load_dotenv()

RAPID_API_KEY = os.getenv('RAPID_API_KEY')
API_URI = os.getenv('API_URI')

