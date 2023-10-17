import discord
import logging
from dotenv import load_dotenv
import os
import time
import Modules.ical_checker as ical_checker

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

    def get_cuurent_date(self):
        while True:
            current_time = time.strftime('%Y-%m-%d %H:%M:%S')


            if current_time.split(" ")[1] == "20:32:00":
                termine = ical_checker.check_calendar_for_date(current_time.split(" ")[0])
                if termine:
                    print(f"Termin: {termine[0]}\nBeschreibung: {termine[1]}Startzeit: {termine[2]}\nEndzeit: {termine[3]}\n")
                    continue




            #time.sleep(60)  # Sleep for 60 seconds (1 minute)

try:
    load_dotenv()  # Load .env file
    token = os.getenv('DISCORD_TOKEN')

    if token:
        # Your bot token has been successfully loaded
        print("Bot token loaded!")

        intents = discord.Intents.default()
        intents.message_content = True
        discord.utils.setup_logging(level=logging.INFO, root=True)
        client = MyClient(intents=intents)


        client.run(token)
        client.get_cuurent_date()

    else:
        print("Bot token not found! Check your .env file.")
        exit()

except Exception as e:
    print(f"Error loading the bot token: {e}")