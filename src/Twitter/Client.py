import requests
import dotenv
import os


class Client:

    def __init__(self, BEARER_TOKEN):
        self.token = BEARER_TOKEN


    def twitter_authorization(self, BEARER_TOKEN):
        url = "https://api.twitter.com/2/tweets/search/recent?query=from:JagexClock Amlodd"
        # parâmetros de requisição
        payload = {}
        headers = {
            'Authorization': f'{BEARER_TOKEN}',
            'Cookie': 'guest_id=v1%3A165048824367222984'}

        return url, payload, headers



    def boss_request(self, url, headers, payload):
        boss = requests.request("GET", url, headers=headers, data=payload)
        bosses = boss.json()

        return bosses

if __name__ == '__main__':
    main()