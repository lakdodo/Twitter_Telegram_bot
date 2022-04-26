import requests
import telebot

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

#Criando lista para adição da lista de texto contendo os boss de Amlodd
list = []
for item in bosses['data']:
  list.append(item['text'])

print(list)


# Autenticação do bot Telegram com telebot
bot_token = '5387498318:AAGyPD5SqqfVzmdlP3hMOT3hieQoCHBXEl8'
bot = telebot.TeleBot(bot_token)

#método de polling dentro do telegram (para trazer a ultima postagem de Amlodd como resposta para qualquer mensagem enviada)
def verificar(mensagem):
 return True

#Devolutiva com ultimo post sobre Amlodd
@bot.message_handler(func=verificar)
def responder(mensagem):
  bot.reply_to(mensagem, list)
bot.polling()



