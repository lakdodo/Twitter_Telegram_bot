import requests
import telebot


# Autenticação do bot Telegram com telebot
bot_token = '5387498318:AAGyPD5SqqfVzmdlP3hMOT3hieQoCHBXEl8'
bot = telebot.TeleBot(bot_token)


# URL de requisição
url = "https://api.twitter.com/2/tweets/search/recent?query=from:JagexClock Amlodd"

#parâmetros de requisição
payload={}
headers = {
  'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAKe3bgEAAAAAEFHYokZm97b%2Bqpf38Lsw3y6gkhY%3DK0VRdzPIuvxRL7F7NLTs7kXvLrbXsK1kcGUuPCWwhxtSbSG2BM',
  'Cookie': 'guest_id=v1%3A165048824367222984'
}
#requisição
boss = requests.request("GET", url, headers=headers, data=payload)
bosses = boss.json()

#Realizando envio de mensagens contendo a localização e hora dos boss

for item in bosses['data']:
  list.append(item['text'])
  bot.send_message(chat_id=2033465314,text=item['text'] )
  print(item['text'])

bot.polling()



