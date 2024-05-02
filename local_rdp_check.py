import discord
import psutil
import os
import getpass
import json
import datetime
import requests
import winreg

# Discord bot token and webhook URL
TOKEN = 'BOT_TOKEN_GOES_HERE'
WEBHOOK_URL = 'WEBHOOK_URL_GOES_HERE'

intents = discord.Intents.all()
client = discord.Client(intents=intents)

# Function to check RDP connection status
def check_rdp_connections():
    rdp_connections = False
    for conn in psutil.net_connections():
        if conn.status == 'ESTABLISHED' and conn.laddr.port == 3389:  # RDP port
            rdp_connections = True
            break
    return rdp_connections

# Function to check if RDP is enabled
def check_rdp_enabled():
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\Terminal Server", 0, winreg.KEY_READ)
        value, _ = winreg.QueryValueEx(reg_key, "fDenyTSConnections")
        winreg.CloseKey(reg_key)
        return value == 0  # RDP is enabled if the value is 0
    except FileNotFoundError:
        return False  # Return False if the registry key is not found

# Function to check if workstation is logged in
def is_logged_in():
    # Check if there is a user logged in to the console session
    session_name = os.environ.get('SESSIONNAME')
    if session_name == 'Console':
        return True
    else:
        return False

# Function to send RDP status update to Discord channel
def send_status_update():
    # Check RDP connection status
    rdp_status = check_rdp_connections()

    # Check if RDP is enabled
    rdp_enabled = check_rdp_enabled()

    # Check if workstation is logged in
    logged_in = is_logged_in()

    # Send status update to Discord webhook
    data = {
        "content": None,
        "embeds": [
            {
                "title": "RDP Status Update",
                "description": f"A remote session is currently {'happening' if rdp_status else 'not happening'}. RDP connections are {'allowed' if rdp_enabled else 'not allowed'}.",
                "color": 13632027 if rdp_status else 16711680,
                "fields": [
                    {
                        "name": "Workstation In Use",
                        "value": f"{'Yes' if logged_in else 'No'}",
                        "inline": True
                    },
                    {
                        "name": "Workstation",
                        "value": f"{getpass.getuser()}",
                        "inline": True
                    }
                ],
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        ]
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(WEBHOOK_URL, data=json.dumps(data), headers=headers)

# Bot command to check RDP status and send update to Discord channel
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!rdpstatus'):
        await message.delete()  # Delete the user's command message
        send_status_update()

# Start the Discord client
client.run(TOKEN)