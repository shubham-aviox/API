import discord
from discord import Webhook, RequestsWebhookAdapter
client = discord.Client()
url = 'https://discord.com/api/webhooks/969484294533808178/w58Ica9C7SmubFVEn93JKPFiSuWDRjnN0k6e7nhGlKGfU2Q9cY0X3BC1WWC3AZkuU175'

webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())
webhook.send(content="Hello this is test meassage") # Executing webhook.

# webhook.send(file=discord.File('demo.py'), content="Hello this is test meassage")