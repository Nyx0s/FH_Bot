import discord
import logging
from dotenv import load_dotenv
import os
import time
import Modules.ical_checker as ical_checker

class MyClient(discord.Client):
    async def on_ready(self):
        # This function is called when the bot is ready and logged in.
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # This function is called when the bot receives a message.
        # It logs information about the received message.
        logging.info(f'Message from {message.author}: {message}')

    def get_cuurent_date(self):
        while True:
            current_time = time.strftime('%Y-%m-%d %H:%M:%S')

            if current_time.split(" ")[1] == "20:32:00":
                # If the current time is 20:32:00, check the calendar for events.
                termine = ical_checker.check_calendar_for_date(current_time.split(" ")[0])
                if termine:
                    # If events are found, print event details.
                    print(f"Termin: {termine[0]}\nBeschreibung: {termine[1]}\nStartzeit: {termine[2]}\nEndzeit: {termine[3]}\n")
                    continue

            # Uncomment the next line if you want to add a 60-second delay between checks.
            # time.sleep(60)

try:
    load_dotenv()  # Load .env file
    token = os.getenv('DISCORD_TOKEN')

    if token:
        # Your bot token has been successfully loaded
        print("Bot token loaded!")

        intents = discord.Intents.default()
        intents.message_content = True
        discord.utils.setup_logging(level=logging.INFO, root=False)
        client = MyClient(intents=intents)

        # Start the bot and the get_cuurent_date function.
        client.run(token)
        client.get_cuurent_date()

    else:
        print("Bot token not found! Check your .env file.")
        exit()

except Exception as e:
    print(f"Error loading the bot token: {e}")
