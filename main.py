import src.Twitter.Client  as TWC
import src.Telegram.Client  as TEC
import dotenv
import os

# Load all the credentials in the env file
dotenv.load_dotenv(dotenv.find_dotenv())
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
TELE_TOKEN = os.getenv("TELE_TOKEN")

# Request the tweets
url,payload,headers = TWC.Client.twitter_authorization(BEARER_TOKEN)
BOSSES = TWC.Client.boss_request(url,headers,payload)

# Send the text of the tweets requested to an specific chat on Telegram
bot = TEC.Client.telegram_authorization(TELE_TOKEN)
send_boss_list = TEC.Client.send_message(BOSSES,bot, CHAT_ID)
