import requests
from icalendar import Calendar
from datetime import datetime


class Kalender():

    def __init__(self, ical_summary, ical_description, ical_start, ical_end):

        self.ical_summary = ical_summary
        self.ical_description = ical_description
        self.ical_start = ical_start
        self.ical_end = ical_end






calendar_url = 'https://cis.fhstp.ac.at/addons/STPCore/cis/meincis/cal.php?tiny=stp630cbb545bb6a'  # Ersetzen Sie dies durch die tatsächliche URL des iCal-Kalenders
response = requests.get(calendar_url)

if response.status_code == 200:
    calendar_data = response.text

else:
    print(f"Fehler beim Abrufen des Kalenders. Statuscode: {response.status_code}")
    exit()

cal = Calendar.from_ical(calendar_data)

if __name__ == "__main__":
    for event in cal.walk('vevent'):
        summary = event.get('summary')
        description = event.get('description')
        start = event.get('dtstart').dt
        end = event.get('dtend').dt
        print(f"Termin: {summary}\nBeschreibung: {description}Startzeit: {start}\nEndzeit: {end}\n")
