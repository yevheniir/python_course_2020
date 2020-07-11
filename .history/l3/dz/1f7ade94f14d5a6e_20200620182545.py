import discord
import random

choose = ('камень(к)', 'ножницы(н)', 'бумага (б)')
TOKEN = 'NzIyMTUwODE5ODQzMjc2ODEz.Xue5ZQ.LSgI49B8JWHQjjCoxFGjOXMLsI4'

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    z = random.choice(choose)
    msg = z.format(message)
    await message.channel.send(msg)
    if (message.content.startswith('к') and z == ('бумага (б)')) or (message.content.startswith('н') and z == ('камень(к)')) or (message.content.startswith('б') and z == ('ножницы(н)')):
        msg = 'GG'.format(message)
        await message.channel.send(msg)
    elif (message.content.startswith('к') and z == ('ножницы(н)')) or (message.content.startswith('б') and z == ('камень(к)')) or (message.content.startswith('н') and z == ('бумага (б)')):
        msg = "WP".format(message)
        await message.channel.send(msg)
    else:
        msg = "Ну шо сказать...".format(message)
        await message.channel.send(msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
