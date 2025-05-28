import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot bejelentkezett mint {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.lower().strip()

    if content == "code":
        await message.channel.send("tc9u9cdg")
