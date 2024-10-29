from datetime import date, timedelta
import random
from database.queries import get_daily_temperature, get_temperature_range

def get_daily_temperatures(target_date):
    result = get_daily_temperature(target_date)
    if result:
        # Assuming you want 24 hourly values, we'll use the average temperature
        return [result.avg_temp] * 24
    else:
        print(f"No data available for {target_date}, using random generation")
        return [random.randint(20, 35) for _ in range(24)]

def get_today_temperature():
    """Retrieve today's temperature data"""
    today = date.today()
    temp = get_daily_temperature(today)
    if temp:
        print(f"Today's temperature: Max {temp.max_temp}, Min {temp.min_temp}, Avg {temp.avg_temp}")

def get_last_7_days_temperatures():
    """Retrieve temperature data for the last 7 days"""
    today = date.today()
    for i in range(7):
        date_ = today - timedelta(days=i)
        temp = get_daily_temperature(date_)
        if temp:
            print(f"{date_}: Max {temp.max_temp}, Min {temp.min_temp}, Avg {temp.avg_temp}")

if __name__ == "__main__":
    today = date.today()
    temperature_data = get_daily_temperatures(today)
    print(f"Today's temperatures: {temperature_data}")
    get_today_temperature()
    get_last_7_days_temperatures()

    # Example of getting data for a range of dates
    last_week = today - timedelta(days=7)
    weekly_data = get_temperature_range(last_week, today)
    if weekly_data:
        print("Weekly temperature summary:")
        for temp in weekly_data:
            print(f"{temp.date}: Max {temp.max_temp}, Min {temp.min_temp}, Avg {temp.avg_temp}")
    else:
        print("No weekly data available")