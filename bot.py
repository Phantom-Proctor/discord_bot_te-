import discord
import os
import random


from dotenv import load_dotenv

load_dotenv()


client = discord.Client()
token=os.getenv("TOKEN")

Greetings = ['Yo', 'Hey there', 'Wagwan','What sup, boss','Greetings Human',]

usr_in2=[""]

usr_in = ['hi','hey','sup','yo','how are you']

@client.event
async def on_ready():
  print(f'{client.user} has connected')

@client.event
async def on_demand():
  print("logged in as {user}".format(client))



@client.event 
async def on_member_join(member):
  await member.create_dm()
  await member.dm_channel.send(
        f'Hi {member.name}, Welcome Klutz'
    )

@client.event
async def on_message(message):
  msg = message.content.lower()
  
  
  if message.author == client.user:
        return 'Ser Jorah /n "A loyal friend and an adviser"'
  
  
  if any(word in msg for word in usr_in ):
    await message.channel.send(random.choice(Greetings))




client.run(token)
