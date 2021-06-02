import discord
import os
import requests
import json
import random

client = discord.Client()
sad_words = ["ЭТБ", "ಠ_ಠ", "ლ(ಠ益ಠლ)", "(ʘᗩʘ')", "ел+", "٩◔̯◔۶", "┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻"]
starter_encouragements = [
 # "хватит есть",
  #"шо, опять??",
  "hah этб",
  "٩◔̯◔۶ этб",
  "hey сhatterbox! let's hook up ddos this этб chat!"
  #"Wo ich herkomme, arbeiten alle hart...",  
  #"Arbeiten!",
  #"Ein paar Stunden arbeiten wir gern!"
  # "вчера же ел, не?."
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('Запущен бот {0.user}'.format(client))

@client.event

async def on_member_update (before, after):
        n = after.JOHN
     if n:
     if n.lower().count("Big Brother") > 0:
        last = before.nick
        if last:
            await after.edit(nick=JOHN)
        else:
            await after.edit(nick="COOKIES")




@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content

  if msg.startswith('q1'):
    quote = get_quote()
    await message.channel.send(quote)
    
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

client.run(os.getenv('TOKEN'))


