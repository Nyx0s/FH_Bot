import discord
import logging
from dotenv import load_dotenv
import os
import time

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

    def print_current_time_every_minute(self):
        while True:
            current_time = time.strftime('%Y-%m-%d %H:%M:%S')
            print(f'Current time: {current_time}')
            time.sleep(60)  # Sleep for 60 seconds (1 minute)

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
        client.print_current_time_every_minute()

        client.run(token)

    else:
        print("Bot token not found! Check your .env file.")
        exit()

except Exception as e:
    print(f"Error loading the bot token: {e}")