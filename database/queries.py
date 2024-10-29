from .database import get_session, DailyTemperature

def get_daily_temperature(date):
    session = get_session()
    try:
        return session.query(DailyTemperature).filter(DailyTemperature.date == date).first()
    finally:
        session.close()

def get_temperature_range(start_date, end_date):
    session = get_session()
    try:
        results = session.query(DailyTemperature).filter(
            DailyTemperature.date.between(start_date, end_date)
        ).all()
        return results
    except Exception as e:
        print(f"Error querying database: {e}")
        return None
    finally:
        session.close()
