import src.Twitter.Client  as TWC
import src.Telegram.Client  as TEC
import dotenv
import os
import schedule
import time


def main():
    """Find and load all the credentials to be used"""
    dotenv.load_dotenv(dotenv.find_dotenv())
    BEARER_TOKEN = os.getenv("BEARER_TOKEN")
    CHAT_ID = os.getenv("CHAT_ID")
    TELE_TOKEN = os.getenv("TELE_TOKEN")

    """Create a Twitter Client"""
    twitter_client = TWC.Client(BEARER_TOKEN)

    """Create a Telegram Bot """
    telegram_bot = TEC.Client(TELE_TOKEN, CHAT_ID)

    """Request the tweets"""
    url,payload,headers = twitter_client.twitter_authorization(BEARER_TOKEN)
    REQUEST_LIST = twitter_client.boss_request(url,headers,payload)

    """Send the text of the tweets requested to an specific chat on Telegram"""
    bot = telegram_bot.telegram_authorization(TELE_TOKEN)
    send_boss_list = telegram_bot.send_message(REQUEST_LIST,bot, CHAT_ID)

"""Scheduling the main function to run every 60 minutes """
schedule.every(1).minutes.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
