import requests
from icalendar import Calendar
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env file

def check_calendar_for_date(date_to_check):
    # Retrieve the iCal file from the URL specified in the .env file
    url = os.getenv('ICAL_URL')
    response = requests.get(url)

    if response.status_code == 200:
        ical_text = response.text

        # Create a calendar object from the iCal text
        cal = Calendar.from_ical(ical_text)

        # Parse the date you want to check
        date_to_check = datetime.strptime(date_to_check, '%Y-%m-%d')

        # Check for entries on the specified date
        for event in cal.walk('VEVENT'):
            event_start = event.get('DTSTART').dt
            if event_start.date() == date_to_check.date():
                # If an entry is found on the specified date, return its details
                return event.get('summary'), event.get('description'), event.get('dtstart').dt, event.get('dtend').dt
    return None  # No entry found on this date

