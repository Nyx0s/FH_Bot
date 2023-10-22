# Discord Bot with iCal Event Notifications

This Discord bot is designed to periodically check an iCal calendar feed and send event notifications to a specified Discord channel. It can be configured to check for events multiple times a day and avoids sending duplicate notifications.

## Prerequisites

Before using this bot, make sure you have the following prerequisites in place:

- **Python:** The bot is written in Python and requires Python 3.6 or higher.

- **Python Packages:** Ensure you have the necessary Python packages installed. You can install them using pip:


- **Discord Bot Token:** You'll need a Discord bot token to run the bot. You can create a bot and obtain the token from the [Discord Developer Portal](https://discord.com/developers/applications).

- **iCal Feed URL:** Have the URL of the iCal feed you want to track. This is the calendar whose events the bot will monitor.

## Configuration

1. Clone or download this repository to your local machine.

2. Create a `.env` file in the project directory and set the following variables:


Replace `YOUR_DISCORD_BOT_TOKEN` with your bot's token and `YOUR_ICAL_FEED_URL` with the URL of the iCal feed you want to track.

3. Customize the Discord channel where event notifications will be sent. Open the `discord_bot.py` script and replace `self.event_channel_id` with your desired channel ID.

## How it Works

The project consists of two primary components:

1. **iCal Event Checker (`ical_checker.py`)**

- This component checks the specified iCal feed for events on a given date.
- Events found on the specified date are returned as a tuple: `(event_summary, event_description, event_start_time, event_end_time)`.

2. **Discord Bot (`discord_bot.py`)**

- This is the Discord bot created using the `discord.py` library.
- The bot periodically checks the iCal feed for events and sends notifications to the specified Discord channel.
- It avoids sending duplicate event notifications by storing event IDs in a set.

## Running the Bot

1. Run the `discord_bot.py` script:


2. The bot will log in and start running. It will periodically check the iCal feed and send event notifications to the specified channel.

## Customization

- You can customize the frequency of event checks by modifying the code that checks the time (e.g., checking for events at 8:00 AM and 8:00 PM).
- You can also customize the channel where event notifications are sent by changing the `self.event_channel_id` variable in the `MyClient` class.
- If you want to check for events further in advance or at different times, you can adjust the code accordingly.

Feel free to modify and extend this bot to fit your specific needs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
