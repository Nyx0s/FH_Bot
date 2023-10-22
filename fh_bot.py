import discord
import logging
from dotenv import load_dotenv
import os
import datetime
import asyncio
import Modules.ical_checker as ical_checker

# Logging configuration
logging.basicConfig(filename='discord.log', level=logging.INFO, format='%(asctime)s [%(name)s] [%(levelname)s] %(message)s')

class MyClient(discord.Client):
    def __init__(self, intents):
        super().__init__(intents=intents)
        self.event_channel_id =  1072780774463504404  # Replace with your desired channel ID
        self.sent_events = set()  # Store sent events to avoid duplicates

    async def on_ready(self):
        # This function is called when the bot is ready and logged in.
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # This function is called when the bot receives a message.
        if message.author == client.user:
            return

        # It logs information about the received message.
        print(f'Message from {message.author}: {message}')
        logging.info(f'Message from {message.author}: {message}')

    async def run_ical_checker(self):
        while True:
            # Get the current date and time
            current_time = datetime.datetime.now()
            one_day_earlier = current_time - datetime.timedelta(days=-1)
            current_date = one_day_earlier.strftime('%Y-%m-%d')
            current_time_str = current_time.strftime('%H:%M:%S')

            # Check if it's time for the first check (e.g., 8:00 AM)
            if current_time_str >= '08:00:00':
                termine = ical_checker.check_calendar_for_date(current_date)

                if termine:
                    event_id = termine[0]  # Use an appropriate identifier for the event
                    if event_id not in self.sent_events:
                        self.sent_events.add(event_id)
                        event_info = f"Termin: {termine[0]}\nBeschreibung: {termine[1]}\nStartzeit: {termine[2]}\nEndzeit: {termine[3]}\n"
                        channel = self.get_channel(self.event_channel_id)

                        if channel:
                            await channel.send(event_info)

            # Check if it's time for the second check (e.g., 8:00 PM)
            if current_time_str >= '20:00:00':

                termine = ical_checker.check_calendar_for_date(current_date)

                if termine:
                    event_id = termine[0]  # Use an appropriate identifier for the event
                    if event_id not in self.sent_events:
                        self.sent_events.add(event_id)
                        event_info = f"Termin: {termine[0]}\nBeschreibung: {termine[1]}\nStartzeit: {termine[2]}\nEndzeit: {termine[3]}\n"
                        channel = self.get_channel(self.event_channel_id)

                        if channel:
                            await channel.send(event_info)

            await asyncio.sleep(60)  # Sleep for 60 seconds before checking again.

try:
    load_dotenv()  # Load .env file
    token = os.getenv('DISCORD_TOKEN')

    if token:
        # Your bot token has been successfully loaded
        print("Bot token loaded!")

        intents = discord.Intents.default()
        intents.guilds = True
        intents.members = True
        intents.message_content = True
        handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
        client = MyClient(intents=intents)
        client.event_channel_id = 1072780774463504404  # Replace with your desired channel ID

        @client.event
        async def on_ready():
            await client.run_ical_checker()

        # Start the bot and the run_ical_checker function.
        client.run(token, log_handler=handler)

    else:
        print("Bot token not found! Check your .env file.")
        exit()

except Exception as e:
    print(f"Error loading the bot token: {e}")
