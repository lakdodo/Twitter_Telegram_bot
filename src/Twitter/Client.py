import requests
import dotenv
import os


class Client:


    def __init__(self, BEARER_TOKEN):
        self.token = BEARER_TOKEN
        self.query = "from:JagexClock Amlodd"

    def twitter_authorization(self, BEARER_TOKEN):
        url = f"https://api.twitter.com/2/tweets/search/recent?query={self.query}"
        # parâmetros de requisição
        payload = {}
        headers = {
            'Authorization': f'{BEARER_TOKEN}',
            'Cookie': 'guest_id=v1%3A165048824367222984'}

        return url, payload, headers

    def request_tweeter(self, url, headers, payload):
        request_tweets = requests.request("GET", url, headers=headers, data=payload)
        tweets_list = request_tweets.json()

        return tweets_list

if __name__ == '__main__':
    main()