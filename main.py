import time
import schedule
import requests
import src.Twitter.Client  as TWC
import src.Telegram.Client  as TEC
import dotenv
import os


#Find and load all the credentials to be used
dotenv.load_dotenv(dotenv.find_dotenv())
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
TELE_TOKEN = os.getenv("TELE_TOKEN")

def main():

    #Create a Twitter Client
    twitter_client = TWC.Client(BEARER_TOKEN)

    #Create a Telegram Bot
    telegram_bot = TEC.Client(TELE_TOKEN, CHAT_ID)

    #Request the tweets
    url,payload,headers = twitter_client.twitter_authorization(BEARER_TOKEN)
    tweets_list = twitter_client.request_tweeter(url, headers, payload)

    #Send the text of the tweets requested to an specific chat on Telegram
    telegram_bot.send_message(tweets_list)


#Scheduling the main function to run every 60 minutes
schedule.every(2).minutes.do(main)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
