# 38 - Workout Google Sheets

import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("NUTRITION_API_ID")
API_KEY = os.getenv("NUTRITION_API_KEY")
