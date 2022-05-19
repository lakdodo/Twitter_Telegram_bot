import telebot
import dotenv
import os


class Client:

    def __init__(self, TELE_TOKEN, CHAT_ID):
        self.token = TELE_TOKEN
        self.chat_id = CHAT_ID
        self.bot = self.telegram_authorization()

    def telegram_authorization(self):
        # Autenticação do bot Telegram com telebot
        bot = telebot.TeleBot(f'{self.token}')
        return bot

    def send_boss(self, tweets_list):

        for item in tweets_list['data']:
            self.bot.send_message(chat_id='-725883740', text=item['text'])
        self.bot.send_message(chat_id='-725883740', text='-' * 20)


if __name__ == '__main__':
    main()
