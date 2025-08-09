# 38 - Workout Google Sheets

import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("NUTRITION_API_ID")
API_KEY = os.getenv("NUTRITION_API_KEY")
API_URL = "https://trackapi.nutritionix.com"


HTTP_HEADER = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

request_data = {
    "query": input("What was your excercise?: "),
    "gender": "male",
    "weight_kg": 94,
    "height_cm": 173,
    "age": 47,
}

request_url = API_URL + "/v2/natural/exercise"

response = requests.post(url=request_url, data=request_data, headers=HTTP_HEADER)

print(response.status_code)
print(response.json())