import telebot
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
    bot = telebot.TeleBot('5343330299:AAH-5AwBW5WdyB8BX4iWoZQTbzkALo3naLU')

    #Request the tweets
    url,payload,headers = twitter_client.twitter_authorization(BEARER_TOKEN)
    tweets_list = twitter_client.request_tweeter(url, headers, payload)

    #Send the text of the tweets requested to an specific chat on Telegram
    for item in tweets_list['data']:
        bot.send_message(-628994820, item['text'])
    bot.send_message(-628994820, '-' * 20)


#Scheduling the main function to run every 60 minutes
#schedule.every(10).seconds.do(main)

if __name__ == '__main__':
    main()


