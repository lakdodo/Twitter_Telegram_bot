import requests
import dotenv
import os


class Client:


    def __init__(self, TELE_TOKEN, CHAT_ID):
        self.token = TELE_TOKEN
        self.chat_id = CHAT_ID
        self.url_base = f'https://api.telegram.org/bot{self.token}'


    def send_message(self, tweets_list):

        for item in tweets_list['data']:
            response = requests.post(
                url=f'{self.url_base}/sendMessage',
                data={'chat_id': self.chat_id, 'text': f'{item["text"]}'}).json


if __name__ == '__main__':
    main()