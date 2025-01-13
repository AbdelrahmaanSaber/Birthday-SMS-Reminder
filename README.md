# Birthday-SMS-Reminder

I created a small and efficent script uses the Vonage API to send a scheduled SMS message as a birthday reminder.
It schedules the message to be sent once a year on a specified date and time.

Key Features:

*   Schedules SMS messages to be sent annually on a specific date and time.
*   Handles cases where the scheduled date has already passed in the current year, rescheduling for the next year.
*   Includes error handling to catch and report issues with the Vonage API.
*   Uses the schedule library for robust scheduling.
*   Uses the datetime library for accurate date and time management.

This project helps you never forget a birthday again!

# Prerequisites

  Python 3.6 or higher: Make sure you have Python installed on your system. You can download it from python.org.
  Vonage Account: You need a Vonage account to use their SMS API. Sign up for a free trial at vonage.com.
  Vonage API Credentials: Once you have a Vonage account, you'll need your API key and secret. You can find these in your Vonage dashboard.
