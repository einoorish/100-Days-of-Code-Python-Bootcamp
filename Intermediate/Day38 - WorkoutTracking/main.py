import requests
from datetime import datetime

APP_ID = "8087a65f"
API_KEY = "0263f77414212eeb788c2c692b78cfda"

GENDER = "female"
WEIGHT = 50
HEIGHT = 160
AGE = 20

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/ec3d136908c79b389ddbe61f7f451b8d/myWorkouts/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

params = {
 "query": input("How did you exercise today?"),
 "gender": GENDER,
 "weight_kg": WEIGHT,
 "height_cm": HEIGHT,
 "age": AGE
}

# input recognition
response = requests.post(exercise_endpoint, json=params, headers=headers)
result = response.json()

# updating google sheets

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs)

    print(sheet_response.text)
