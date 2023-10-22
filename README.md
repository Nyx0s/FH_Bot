Discord Bot with iCal Event Notifications
This README provides an overview of the Discord bot that sends event notifications using the iCal format. The bot can be configured to periodically check for events in an iCal feed and send event notifications to a designated Discord channel.

Prerequisites
Before you can use the Discord bot and iCal functionality, ensure that you have the following prerequisites:

Python installed on your system (v3.6 or higher).
Necessary Python packages installed, including requests, icalendar, dotenv, and discord.py.
A Discord bot token. You can create a bot and obtain the token from the Discord Developer Portal.
An iCal feed URL for the calendar you want to track.
Configuration
Clone or download the repository to your local machine.

Install the required Python packages using pip:

Copy code
pip install requests icalendar python-dotenv discord.py
Create a .env file in the project directory and add the following variables:

makefile
Copy code
DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
ICAL_URL=YOUR_ICAL_FEED_URL
Replace YOUR_DISCORD_BOT_TOKEN with your bot's token and YOUR_ICAL_FEED_URL with the URL of the iCal feed you want to track.

Update the Discord channel ID in the MyClient class in the code to specify the channel where event notifications will be sent. Replace self.event_channel_id with your desired channel ID.

How it Works
The project consists of two main components:

iCal Event Checker (ical_checker.py)

The check_calendar_for_date(date_to_check) function retrieves the iCal data from the specified URL and parses it to extract event details for a given date.
Events found on the specified date are returned as a tuple: (event_summary, event_description, event_start_time, event_end_time).
Discord Bot (discord_bot.py)

The Discord bot, created using the discord.py library, periodically checks the iCal feed for events using the ical_checker module.
The bot checks for events twice a day (configurable) and sends event notifications to the designated Discord channel.
It avoids sending duplicate event notifications by storing event IDs in a set.
Running the Bot
Execute the discord_bot.py script:

Copy code
python discord_bot.py
The bot will log in and start running. It will periodically check the iCal feed and send event notifications to the specified channel.

Customization
You can customize the frequency of event checks by modifying the code that checks the time (e.g., checking for events at 8:00 AM and 8:00 PM).
You can also customize the channel where event notifications are sent by changing the self.event_channel_id variable in the MyClient class.
If you want to check for events further in advance or at different times, you can adjust the code accordingly.
Feel free to modify and extend this bot to fit your specific needs.