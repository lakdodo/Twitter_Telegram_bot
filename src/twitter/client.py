import requests


class Client:
    """ Class for the twitter api

    Args:
        bearer_token (str): bearer token of the twitter account

    Attributes:
        twitter_query (str): query to search for twitts
        default_url (str): url of the twitter api
        
    """
    
    
    twitter_query = "from:JagexClock Amlodd"
    default_url = "https://api.twitter.com/2/tweets/search/recent?query=" + twitter_query


    def __init__(self, bearer_token):
        """Constructor for the Client class.

        Args:
            bearer_token (str): bearer token of the twitter account
        """
        
        self._token = bearer_token

    def __twitter_authorization_header(self):
        """Generate the authorization header for the twitter api.

        Returns:
            (dict, dict): payload and headers
        """
        
        # parâmetros de requisição
        payload = {}
        headers = {
            'Authorization': f'{self._token}',
            'Cookie': 'guest_id=v1%3A165048824367222984'}
        
        return payload, headers

    def request_twitts(self):
        """Request the twitts from the twitter api.

        Returns:
            Any: Returns the json-encoded content of a response, if any.
        """
        payload, headers = self.__twitter_authorization_header()
        
        twitts = requests.request("GET", self.default_url, headers=headers, data=payload)
        twitts_json = twitts.json()
        
        return twitts_json

