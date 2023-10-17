import requests
from icalendar import Calendar
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env file

def check_calendar_for_date(date_to_check):
    url = os.getenv('ICAL_URL')
    # iCal-Datei von der URL abrufen
    response = requests.get(url)

    if response.status_code == 200:
        ical_text = response.text

        # Kalenderobjekt erstellen
        cal = Calendar.from_ical(ical_text)

        # Datum, das Sie überprüfen möchten
        date_to_check = datetime.strptime(date_to_check, '%Y-%m-%d')

        # Überprüfen, ob es Einträge an diesem Datum gibt
        for event in cal.walk('VEVENT'):
            event_start = event.get('DTSTART').dt
            if event_start.date() == date_to_check.date():
                return event.get('summary'), event.get('description'), event.get('dtstart').dt, event.get('dtend').dt
    return None  # Kein Eintrag an diesem Datum gefunden

if __name__ == "__main":
    termine = check_calendar_for_date("2023-10-17")
    if termine:
        print(f"Termin: {termine[0]}\nBeschreibung: {termine[1]}\nStartzeit: {termine[2]}\nEndzeit: {termine[3]}\n")
    else:
        print("Kein Termin gefunden.")