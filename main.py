import discord
import os
import requests
import json
import random

client = discord.Client()
dict_words = [
"!1",
"!2"
]
dict_answers2 = [
  "хватит есть",
  "шо, опять??",
  "hah этб",
  "Wo ich herkomme, arbeiten alle hart...",  
  "Arbeiten!",
  "Ein paar Stunden arbeiten wir gern!"
  "вчера же ел, не?."
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random") 
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)
 
def get_cat():
  response = requests.get("https://some-random-api.ml/img/cat")
  json_data = json.loads(response.text)
  quote = json_data['link']
  return(quote)

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content

  if msg.startswith('!cat'):
    quote = get_cat()
    await message.channel.send(quote)
    
  if any(word in msg for word in dict_words):
    await message.channel.send(random.choice(dict_answers2))

@client.event
async def on_ready():
  print('# эхо + картинки + цитаты #') 
  print('Запущен бот {0.user}'.format(client))    

#client.run(os.getenv('TOKEN'))


client.run(ODIzNDkyNjM1MTMzNzM5MDc4.YFhnRw.MCj4TksI44UBcdd9g4p0O7qA7yg)