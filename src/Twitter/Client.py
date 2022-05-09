import requests
import dotenv
import os


dotenv.load_dotenv(dotenv.find_dotenv())
BEARER_TOKEN = os.getenv("BEARER_TOKEN")


class Client:

    def __init__(self):
        self.token = BEARER_TOKEN

    def twitter_authorization(token):
        url = "https://api.twitter.com/2/tweets/search/recent?query=from:JagexClock Amlodd"
        # parâmetros de requisição
        payload = {}
        headers = {
            'Authorization': f'{token}',
            'Cookie': 'guest_id=v1%3A165048824367222984'}
        return url, payload, headers

    def boss_request(url, headers, payload):
        boss = requests.request("GET", url, headers=headers, data=payload)
        bosses = boss.json()
        return bosses
