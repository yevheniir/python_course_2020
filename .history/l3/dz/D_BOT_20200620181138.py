import discord
import random

choose=["paper", "rock", "scissors"];
TOKEN='NzIyODM1MTUzMTk3NzI3ODE1.Xuo2vg.zshqqzdi812meszyrdJBRc0O3tg'

client=discord.Client()

@client.event
async def on_message(message):\

        if message.author==client.user:
                return
        x = random.choice(choose)
        msg=x.format(message)
        await message.channel.send(msg)
        if (message.content.startswith('rock') and x==('paper')) or (message.content.startswith('scissors') and x==('rock')) or (message.content.startswith('paper') and x==('scissors')):
                msg='Lose'.format(message)
                await message.channel.send(msg)
                win_bot=win_bot+1
        if (message.content.startswith('rock') and x==('scissors')) or (message.content.startswith('paper') and x==('rock')) or (message.content.startswith('scissors') and x==('paper')):
                msg="Win".format(message)
                await message.channel.send(msg)
                win_player=win_player+1
        else:
        	msg="Draw".format(message)
        	await message.channel.send(msg)
        msg=win_bot.format(message)
        msg=win_player.format(message)
        await message.channel.send(msg)
        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
