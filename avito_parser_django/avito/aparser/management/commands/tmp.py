import requests
import os
url = 'https://icanhazdadjoke.com/'
headers = {'Accept': 'application/json'}


def sofiaResponse(audio):
    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)


res = requests.get(
    'https://icanhazdadjoke.com/',
    headers={"Accept": "application/json"})
if res.status_code == requests.codes.ok:
    sofiaResponse(str(res.json()['joke']))
else:
    print(res.status_code)
    sofiaResponse('oops!I ran out of jokes')

# joke_msg = requests.get(url, headers=headers).json().get('joke')
# print(joke_msg)

# from discord.ext import commands
# import requests
# import discord
# import asyncio
#
#
# intents = discord.Intents.all()
# bot = commands.Bot(command_prefix= "?", intents=intents)
#
#
#
# @bot.command()
# async def foo(ctx, arg):
#     await ctx.send(arg)
#
#
# @bot.command()
# async def on_ready():
#     print("bot online")
#
#
# @bot.command()
# async def on_message(message):
#     if message.author == bot.id:
#         return
#
#     if message.content == "ana":
#         await message.channel.send("baban")
#
# @bot.command()
# async def start_count(ctx):
#             key = "some-crypto-shit-api"
#             data = requests.get(key)
#             data = data.json()
#             price = data["price"]
#             coin = data["symbol"]
#             await ctx.send(price)
#
#
# bot.add_command(start_count)
# bot.run('my_Token')
