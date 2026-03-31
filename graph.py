import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pooja@2003",
    database="weather_db"
)

# fetch data
query = "SELECT recorded_at, temperature FROM weather_data"
df = pd.read_sql(query, conn)

# print data
print(df)

# plot graph
plt.figure()
plt.plot(df['recorded_at'], df['temperature'])
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("Temperature Trend")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()