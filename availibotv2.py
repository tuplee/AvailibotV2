import discord
import requests

intents= discord.Intents.all()

client = discord.Client(intents=intents)

API_URL = 'https://x.pythonanywhere.com/retrieve_RDPStatus'

@client.event
async def on_ready():
    print('Logged in as', client.user.name)

@client.event
async def on_message(message):
    if message.content.startswith('!rdp_status'):
        response = requests.get(API_URL)
        data = response.json()
        rdp_status = data.get('rdp_status', False)
    
        if rdp_status:
            await message.channel.send('RDP connection is active.')
        else:
            await message.channel.send('RDP connection is not active.')

client.run('BotTokenGoesHere')