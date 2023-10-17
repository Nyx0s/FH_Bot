import requests
from icalendar import Calendar

calendar_url = 'https://cis.fhstp.ac.at/addons/STPCore/cis/meincis/cal.php?tiny=stp630cbb545bb6a'  # Ersetzen Sie dies durch die tatsächliche URL des iCal-Kalenders
response = requests.get(calendar_url)

if response.status_code == 200:
    calendar_data = response.text
    
else:
    print(f"Fehler beim Abrufen des Kalenders. Statuscode: {response.status_code}")
    exit()
    
cal = Calendar.from_ical(calendar_data)

for event in cal.walk('vevent'):
    summary = event.get('summary')
    start = event.get('dtstart').dt
    end = event.get('dtend').dt
    print(f"Termin: {summary}\nStartzeit: {start}\nEndzeit: {end}\n")