from dotenv import load_dotenv, find_dotenv
import os
import telegram
import twitter



def main():
    # Load all the credentials in the env file
    load_dotenv(find_dotenv())
    
    BEARER_TOKEN = os.getenv("BEARER_TOKEN")
    CHAT_ID = os.getenv("CHAT_ID")
    TELE_TOKEN = os.getenv("TELE_TOKEN")
    
    
    # Create the telegram client
    telegram_bot = telegram.Client(TELE_TOKEN, CHAT_ID)

    # Create the twitter client
    twitter_client = twitter.Client(BEARER_TOKEN)
    # Get the twitts from the twitter client
    twiits_msgs = twitter_client.request_twitts()
    
    # Send the text of the tweets requested to an specific chat on Telegram
    telegram_bot.send_message(twiits_msgs)
    

if __name__ == '__main__':
    main()
    
    
