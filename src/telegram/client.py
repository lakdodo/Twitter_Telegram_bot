import telebot

class Client:
    """ Class for the telegram bot api

    Args:
        tele_token (str): token of the telegram bot
        chat_id (str): chat id of the telegram desired chat

    Attributes:
        token (str): token of the telegram bot
        chat_id (str): chat id of the telegram desired chat
        bot (obj): bot object
        
    """

    def __init__(self,tele_token : str,chat_id : str) :
        """Constructor for the Client class.

        Args:
            tele_token (str): token of the telegram bot
            chat_id (str): chat id of the telegram desired chat
        """
        self._token = tele_token
        self._chat_id = chat_id
        self._bot = self.__authentication()

    def __authentication(self):
        """ Authenticate the bot with the telegram api.

        Returns:
            Telebot : Telebot object
        """
        # Autenticação do bot Telegram com telebot
        bot = telebot.TeleBot(f'{self._token}')
        return bot

    def send_message(self, text_message):
        """Send a message to the telegram chat.

        Args:
            text_message (any): message to be sent
        """
        
        for item in text_message['data']:
            self._bot.send_message(chat_id=self._chat_id, text=item['text'])
            
        self._bot.send_message(chat_id=self._chat_id, text='-' * 20)