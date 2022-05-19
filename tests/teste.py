import requests
import src.Twitter.Client as TWC
import dotenv
import os


dotenv.load_dotenv(dotenv.find_dotenv())
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
TELE_TOKEN = os.getenv("TELE_TOKEN")


twitter_client = TWC.Client(BEARER_TOKEN)

url,payload,headers = twitter_client.twitter_authorization(BEARER_TOKEN)
tweets_list = twitter_client.request_tweeter(url, headers, payload)
teste = tweets_list['data'][0]['text']

teste = teste.replace('UTC','GMT-3')
print(teste[0:])
teste2 = teste[-12:-10]
teste2 = int(teste2)
teste2 = teste2 + 3
teste2 = str(teste2)
print(teste2)