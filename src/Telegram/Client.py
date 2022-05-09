import telebot
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())
TELE_TOKEN = os.getenv("TELE_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


class Client:

    def __init__(self):
        self.token = TELE_TOKEN
        self.chat_id = CHAT_ID

    def telegram_authorization(TELE_TOKEN):
        # Autenticação do bot Telegram com telebot
        bot = telebot.TeleBot(f'{TELE_TOKEN}')
        return bot

    def send_message(bosses, bot):

        for item in bosses['data']:
            bot.send_message(chat_id=CHAT_ID, text=item['text'])
        bot.send_message(chat_id=CHAT_ID, text='-' * 20)
