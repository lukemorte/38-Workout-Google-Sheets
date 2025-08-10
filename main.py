# 38 - Workout Google Sheets

import requests
import os
from dotenv import load_dotenv
from test_data import test_data
from datetime import datetime

load_dotenv()

API_ID = os.getenv("NUTRITION_API_ID")
API_KEY = os.getenv("NUTRITION_API_KEY")
API_URL = "https://trackapi.nutritionix.com"


HTTP_HEADER = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

# request_data = {
#     "query": input("Tell me which excercise you did?: "),
#     "gender": "male",
#     "weight_kg": 94,
#     "height_cm": 173,
#     "age": 47,
# }

request_url = API_URL + "/v2/natural/exercise"

# response = requests.post(url=request_url, data=request_data, headers=HTTP_HEADER)
# print(response.status_code)
# print(response.json())

now_formatted = datetime.now().strftime("%d/%m/%Y")
now_time_formatted = datetime.now().strftime("%H:%M")


# print(now_formatted)

for item in test_data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": now_formatted,
            "time": now_time_formatted,
            "excercise": item["name"].title(),
            "duration": item["duration_min"],
            "calories": item["nf_calories"],
        }
    }

    x_header = {
        "Authorization": "Basic eHVzZXI6ZGVmeDE0",
        "Content-Type": "application/json",
    }

    print(sheet_inputs)

    BASIC_USERNAME = "xuser"
    BASIC_PASSWORD = "defx14"
    sheet_request_url = "https://api.sheety.co/5f2e71425f09ba9a917864d228b52ef4/myWorkouts/workouts"
    response = requests.post(url=sheet_request_url, json=sheet_inputs, headers=x_header, auth=(BASIC_USERNAME, BASIC_PASSWORD))
    print(response.status_code)
