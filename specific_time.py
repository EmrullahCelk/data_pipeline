from datetime import datetime
from weather_information import weather_info
from send_mail import send_email
import time





def query_at_specific_time():
    while True:
        try:
            target_hour = 13
            target_minute = 44
            now = datetime.now()

            target_time = datetime(now.year, now.month, now.day, target_hour, target_minute)

            if now >= target_time:
                weather_info()
                break
            else:

                time.sleep(60)

        except Exception as e:

            send_email(subject="Error at query_at_specific_time function", body=f"operation could not be completed. Error:{e}")
            time.sleep(60)