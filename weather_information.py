import requests
from datetime import datetime
from create_dataframe import create_dataframe_from_weather
from df_to_postgrsql import write_dataframe_to_postgres
from send_mail import send_email
from dotenv import load_dotenv
from os import getenv


load_dotenv()

def weather_info():

    api_key = getenv("api_key")
    city = getenv("city")
    base_url = getenv("base_url")

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            df = create_dataframe_from_weather(data)
            write_dataframe_to_postgres(df)

            send_email(subject=f"statuscode: {response.status_code}", body="operation completed successfully")
        else:
            send_email(subject=f"statuscode: {response.status_code}", body=f"operation could not be completed. Error:{e}")

    except Exception as e:
        send_email(subject=f"statuscode: {response.status_code}", body=f"operation could not be completed. Error:{e}")
