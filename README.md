# README

## Calendar and Discord Bot

This GitHub repository contains two Python scripts: one for checking events in an iCalendar (iCal) file, and another for a Discord bot that provides event notifications. The owner of this repository is Nyx0s.

### 1. `ical_checker.py`

#### Usage

This script allows you to check for events in an iCalendar file located at a specified URL. It can be useful for retrieving and displaying events for a given date. To use the script, follow these steps:

1. **Prerequisites:**
   - Python 3.x installed.
   - Required Python packages can be installed using `pip install icalendar requests python-dotenv`.

2. **Configuration:**
   - Create a `.env` file in the same directory as the script and set the following variables:
     ```
     ICAL_URL=<URL_of_the_iCal_file>
     ```

3. **Running the Script:**
   - Run the script in your terminal:
     ```
     python ical_checker.py
     ```
   - The script will check for events on the date specified in the `if __name__ == "__main__":` block and display event details if found.

### 2. `discord_bot.py`

#### Usage

This script sets up a Discord bot using the Discord API and the `discord.py` library. The bot continuously checks for events in an iCalendar file and provides event notifications in a specific channel at a designated time. To use the script, follow these steps:

1. **Prerequisites:**
   - Python 3.x installed.
   - Required Python packages can be installed using `pip install discord.py python-dotenv`.

2. **Configuration:**
   - Create a `.env` file in the same directory as the script and set the following variables:
     ```
     DISCORD_TOKEN=<Your_Discord_Bot_Token>
     ```

3. **Running the Script:**
   - Run the script in your terminal:
     ```
     python discord_bot.py
     ```
   - The bot will log in and continuously check for events at the specified time (in this example, at 20:32:00). If an event is found, it will post event details in the configured channel on Discord.

### 3. Discord Bot Integration

To use the Discord bot script, you will need to invite the bot to your server and set up the Discord channel where event notifications will be sent. You can customize the bot's behavior by modifying the `get_cuurent_date` method in the `discord_bot.py` script.

For any questions or issues, please contact the owner of this repository, Nyx0s.

Enjoy using the Calendar and Discord Bot scripts!
