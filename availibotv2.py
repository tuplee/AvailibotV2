import discord
import requests

intents= discord.Intents.all()
#intents.message = True

client = discord.Client(intents=intents)

# API URL of your Flask app
API_URL = 'https://doggthebountyhunter.pythonanywhere.com/get-rdp-status'

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

# Replace 'YOUR_DISCORD_BOT_TOKEN' with your actual Discord bot token
client.run('MTIzMzE0OTU3ODM0MjMwNTgzMg.GsY44F.Cu0Dwv2FRdAGLNQ9hAmS6GCEvqgEIeBi_IkjhI')