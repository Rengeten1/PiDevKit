import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry

def get_today_sunset(latitude=52.52, longitude=13.41):
    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    # API request
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "sunset",
        "forecast_days": 1
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process daily data
    daily = responses[0].Daily()
    daily_sunset = daily.Variables(0).ValuesInt64AsNumpy()
    daily_data = {
        "date": pd.date_range(
            start=pd.to_datetime(daily.Time(), unit="s", utc=True),
            end=pd.to_datetime(daily.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=daily.Interval()),
            inclusive="left"
        )
    }
    daily_data["sunset"] = daily_sunset
    daily_dataframe = pd.DataFrame(data=daily_data)
    daily_dataframe["sunset_time"] = pd.to_datetime(daily_dataframe["sunset"], unit="s", utc=True)

    # Return sunset time as datetime
    sunset_time = daily_dataframe.loc[0, "sunset_time"]
    return sunset_time