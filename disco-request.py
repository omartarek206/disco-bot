import requests
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
API = 'https://discord.com/api'

endpoint = '/guilds/'
auth_header = {'Authorization': f'Bot {TOKEN}'}

url = API + endpoint + GUILD
print(url)
headers = {
    'Authorization': auth_header['Authorization']
    }
print(headers)
r = requests.get(url, headers=headers)

print(r.status_code)
print(r.text)
print(r.json())
