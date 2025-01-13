import vonage
import schedule
import time
import datetime

def send_birthday_message():
  
    try:
        client = vonage.Client(key="829de702", secret="FzpW5qQGe6HYVKHU")
        sms = vonage.Sms(client)
        responseData = sms.send_message(
            {
                "from": "Remember Me",
                "to": "201555095508",
                "text": "Birthday Message KA",
            }
        )
        print(f"Done..  : {responseData}")  
    except vonage.VonageError as e:
        print(f"Error send {e}") 
    except Exception as e: 
        print(f"Error happened: {e}")

def schedule_birthday_message(year, month, day, hour=0, minute=0):

    scheduled_date = datetime.datetime(year, month, day, hour, minute)
    now = datetime.datetime.now()

    if scheduled_date < now: 
        scheduled_date = datetime.datetime(now.year + 1, month, day, hour, minute) 
        print(f"The date passed this year rescheduled to {scheduled_date}")
    else:
        print(f"The message is scheduled for {scheduled_date}")

    #schedule
    schedule.every().year.at(scheduled_date.strftime("%Y-%m-%d %H:%M")).do(send_birthday_message)

if __name__ == "__main__":
    # ex: 26 / 4  12:00 Am
    target_month = 4 #April month
    target_day = 26  #Day 26
    target_hour = 12 
    target_minute = 0
    schedule_birthday_message(datetime.datetime.now().year,target_month, target_day, target_hour, target_minute)

    while True:
        schedule.run_pending()
        time.sleep(1)