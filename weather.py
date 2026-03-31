import requests
import mysql.connector

# 🛢️ MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pooja@2003",
    database="weather_db"
)

cursor = conn.cursor()

# ✅ FREE API (no key needed)
url = "https://api.open-meteo.com/v1/forecast?latitude=19.07&longitude=72.87&current_weather=true"

data = requests.get(url).json()

print("API RESPONSE:", data)

# extract data
temp = data['current_weather']['temperature']
hum = 0
weather = "clear"

# insert into DB
cursor.execute(
    "INSERT INTO weather_data (city, temperature, humidity, weather_desc) VALUES (%s,%s,%s,%s)",
    ("Mumbai", temp, hum, weather)
)

conn.commit()

print("✅ DONE - DATA INSERTED")

import time

while True:
    # your whole code inside a function OR paste logic here
    data = requests.get(url).json()

    print("API RESPONSE:", data)

    temp = data['current_weather']['temperature']
    hum = 0
    weather = "clear"

    cursor.execute(
        "INSERT INTO weather_data (city, temperature, humidity, weather_desc) VALUES (%s,%s,%s,%s)",
        ("Mumbai", temp, hum, weather)
    )

    conn.commit()

    print("✅ DONE - DATA INSERTED")

    time.sleep(300)   # every 5 minutes