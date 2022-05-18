import telebot
import dotenv
import os


class Client:
    """ The constructor will initiate with these 2 attributes, the telegram token and
     the target chat, that will receive the tweets."""
    def __init__(self, TELE_TOKEN, CHAT_ID):
        self.token = TELE_TOKEN
        self.chat_id = CHAT_ID
    """This authorization is needed to create the client in the main module"""
    def telegram_authorization(self, TELE_TOKEN):
        # Autenticação do bot Telegram com telebot
        bot = telebot.TeleBot(f'{TELE_TOKEN}')
        return bot
    """The send_message function will send the tweets encapsulated"""
    def send_message(self, bosses, bot, CHAT_ID):

        for item in bosses['data']:
            bot.send_message(chat_id=CHAT_ID, text=item['text'])
        bot.send_message(chat_id=CHAT_ID, text='-' * 20)


if __name__ == '__main__':
    main()
