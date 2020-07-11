import discord, random, os

#TOKEN = os.environ.get('TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    a = random.choice(choose)
    if message.content.startwith('!start'):
        msg = 'Hello ' + message.author.mention + 'Гра /n !1 - камінь  !2 - ножиці  !3 - бумага'
        await message.channel.send(msg)
    if (message.content.startswith('!1')) and a == ('!1') or (message.content.startswith('!2')) and a == ('!2') or (message.content.startswith('!3')) and a == ('!3'):
        msg = 'Нічия'
        await message.channel.send(msg)
    elif (message.content.startswith('!1')) and a == ('!2'):
        msg=('Ви обрали камінь'/n + 'Бот обрав ножиці'/n + 'Ви перемогли')
        await message.channel.send(msg)
    elif (message.content.startswith('!1')) and a == ('!3'):
        msg=('Ви обрали камінь'/n + 'Бот обрав бумагу'/n + 'Ви програли')
        await message.channel.send(msg)
    elif (message.content.startswith('!2')) and a == ('!1'):
        msg=('Ви обрали камінь'/n + 'Бот обрав камінь'/n + 'Ви програли')
        await message.channel.send(msg)
    elif (message.content.startswith('!2')) and a == ('!3'):
        msg=('Ви обрали камінь'/n + 'Бот обрав ножиці'/n + 'Ви перемогли')
        await message.channel.send(msg)
    elif (message.content.startswith('!3')) and a == ('!1'):
        msg=('Ви обрали камінь'/n + 'Бот обрав ножиці'/n + 'Ви перемогли')
        await message.channel.send(msg)
    if (message.content.startswith('!3')) and a == ('!2'):
        msg=('Ви обрали камінь \n' + 'Бот обрав ножиці'/n + 'Ви програли')
        await message.channel.send(msg)
    
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')
