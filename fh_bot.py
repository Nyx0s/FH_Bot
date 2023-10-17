import discord
import logging
import dotenv
import os
from datetime import datetime
from apscheduler import AsyncScheduler

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')


    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

    async def daily_task(self):
        current_date = datetime.now().strftime('%Y-%m-%d')
        print(f'Daily task executed at midnight. Current Date: {current_date}')

    def run_scheduler(self):
        scheduler = AsyncScheduler()
        scheduler.add_job(self.daily_task, 'interval', seconds=60)  # Code wird alle 60 Sekunden ausgeführt
        scheduler.start()





try:
    dotenv.load_dotenv(dotenv.find_dotenv())
    token = os.getenv('DISCORD_TOKEN')

    if token:



        # Dein Bot-Token wurde erfolgreich geladen
        print("Bot-Token geladen!")

        intents = discord.Intents.default()
        intents.message_content = True
        discord.utils.setup_logging(level=logging.INFO, root=True)
        client = MyClient(intents=intents)
        client.run(token)




    else:
        print("Bot-Token nicht gefunden! Überprüfe deine .env-Datei.")
        exit()

except Exception as e:
    print(f"Fehler beim Laden des Bot-Tokens: {e}")



