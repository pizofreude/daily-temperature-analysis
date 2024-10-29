import requests
from datetime import datetime, timedelta
import pandas as pd
from database.database import DailyTemperature, init_db, get_session

def fetch_temperature_data(latitude, longitude, start_date, end_date):
    """Fetch temperature data from the Open-Meteo API"""
    base_url = "https://api.open-meteo.com/v1/forecast"
    
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "daily": "temperature_2m_max,temperature_2m_min,temperature_2m_mean",
        "timezone": "auto"
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for bad responses
        data = response.json()
        
        df = pd.DataFrame({
            "date": pd.to_datetime(data["daily"]["time"]),
            "max_temp": data["daily"]["temperature_2m_max"],
            "min_temp": data["daily"]["temperature_2m_min"],
            "avg_temp": data["daily"]["temperature_2m_mean"]
        })
        
        return df
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None

def store_temperature_data(df):
    """Store temperature data in the database"""
    session = get_session()
    for _, row in df.iterrows():
        daily_temp = DailyTemperature(
            date=row['date'].date(),
            max_temp=row['max_temp'],
            min_temp=row['min_temp'],
            avg_temp=row['avg_temp']
        )
        session.add(daily_temp)
    session.commit()
    session.close()

if __name__ == "__main__":
    # Initialize the database
    init_db()

    # Set location as Cameron Highlands, Malaysia
    location = {
        "latitude": 4.48134836611477,
        "longitude": 101.37709563633592
    }

    # Set date range
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=30)

    # Fetch temperature data
    temperature_data = fetch_temperature_data(
        location["latitude"],
        location["longitude"],
        start_date.isoformat(),
        end_date.isoformat()
    )

    if temperature_data is not None:
        print(temperature_data.head())
        store_temperature_data(temperature_data)
        print("Temperature data stored in the database.")
    else:
        print("Failed to fetch temperature data.")

# # Set location as Cameron Highlands, Malaysia
# latitude = 4.48134836611477  # Cameron Highlands latitude
# longitude = 101.37709563633592  # Cameron Highlands longitude
# end_date = datetime.now().date()
# start_date = end_date - timedelta(days=30)  # Fetch last 30 days of data

# temperature_data = fetch_temperature_data(
#     latitude, 
#     longitude, 
#     start_date.isoformat(), 
#     end_date.isoformat()
# )

# if temperature_data is not None:
#     print(temperature_data.head())
#     # Here you can add code to store the data in your database
# else:
#     print("Failed to fetch temperature data.")
