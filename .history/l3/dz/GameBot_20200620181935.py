import discord
import random
TOKEN = 'NzIzNTQzNDk1OTc2OTQzNjI2.XuzKbw.sVfmaFwGyA7agglqtgDdoUBKiDA'
list1 = []
client = discord.Client()
bot_player = {}
win_bot = []
win_bot.append(0)
win_player = []
win_player.append(0)
bot_player = {"Бот": win_bot,
              "Игрок": win_player
              }
first_comand = [
    "##################################################",
    " Начать игру - !start   ",
    "##################################################"
]
second_comand = [
    "#################",
    " Вы вышли из игры ",
    "#################"
]


def player():
    win_player.append(win_player[-1]+1)
    bot_player = {"Бот": win_bot[-1],
                  "Игрок": win_player[-1]
                  }


def bot():
    win_bot.append(win_player[-1]+1)
    bot_player = {"Бот": win_bot[-1],
                  "Игрок": win_player[-1]
                  }


def draw():
    bot_player = {"Бот": win_bot[-1],
                  "Игрок": win_player[-1]
                  }
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.content.startswith('!start'):
       # ")
        await message.channel.send("Введи !Камень,!Ножницы или !Бумага")
    if message.content.startswith('!Камень'):
        list1 = []
        list1.append("Камень")
        print(message.author.mention + "\n" +
              "поставил\n"+list1[0].lower()+".\n\n")
        list2 = ['Бумага', 'Камень', 'Ножницы']
        rand = random.choice(list2)
        if(list1[0] == rand):
            await message.channel.send("Бот выбрал  " + rand.lower()+".")
            await message.channel.send("Ничья!")
            bot_player = {"Бот": win_bot[0],
                          "Игрок": win_player[0]
                          }
            await message.channel.send("Бот - " + str(bot_player["Бот"]) + "\n")
            await message.channel.send("Игрок - " + str(bot_player["Игрок"]) + "\n")
            print("\n\nБот - " + str(bot_player["Бот"]) + "\n")
            print("Игрок - " + str(bot_player["Игрок"]) + "\n")
        if(list1[0] == 'Бумага'and rand == 'Камень'):
            await message.channel.send("Бот выбрал  " + rand.lower()+".")
            await message.channel.send("Ты победил")
            win_player.append(win_player[-1]+1)
            bot_player = {"Бот": win_bot[-1],
                          "Игрок": win_player[-1]
                          }
            await message.channel.send("Бот - " + str(bot_player["Бот"]) + "\n")
            await message.channel.send("Игрок - " + str(bot_player["Игрок"]) + "\n")
            print("\n\nБот - " + str(bot_player["Бот"]) + "\n")
            print("Игрок - " + str(bot_player["Игрок"]) + "\n")
        if(list1[0] == 'Камень'and rand == 'Бумага'):
            await message.channel.send("Бот выбрал  " + rand.lower()+".")
            await message.channel.send("Ты проиграл(")
            win_bot.append(win_bot[-1]+1)
            bot_player = {"Бот": win_bot[-1],
                          "Игрок": win_player[-1]
                          }
            await message.channel.send("Бот - " + str(bot_player["Бот"]) + "\n")
            await message.channel.send("Игрок - " + str(bot_player["Игрок"]) + "\n")
            print("\n\nБот - " + str(bot_player["Бот"]) + "\n")
            print("Игрок - " + str(bot_player["Игрок"]) + "\n")
        if(list1[0] == 'Ножницы'and rand == 'Камень'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы проиграли!")
            win_bot.append(win_bot[-1]+1)
            bot_player = {"Бот": win_bot[-1],
                          "Игрок": win_player[-1]
                          }
            await message.channel.send("Бот - " + str(bot_player["Бот"]) + "\n")
            await message.channel.send("Игрок - " + str(bot_player["Игрок"]) + "\n")
            print("\n\nБот - " + str(bot_player["Бот"]) + "\n")
            print("Игрок - " + str(bot_player["Игрок"]) + "\n")
        if(list1[0] == 'Камень'and rand == 'Ножницы'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы победили!")
            win_player.append(win_player[-1]+1)
            bot_player = {"Бот": win_bot[-1],
                          "Игрок": win_player[-1]
                          }
            await message.channel.send("Бот - " + str(bot_player["Бот"]) + "\n")
            await message.channel.send("Игрок - " + str(bot_player["Игрок"]) + "\n")
            print("\n\nБот - " + str(bot_player["Бот"]) + "\n")
            print("Игрок - " + str(bot_player["Игрок"]) + "\n")
        if(list1[0] == 'Бумага'and rand == 'Ножницы'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы проиграли!")
            win_bot.append(win_bot[-1]+1)
            bot_player = {"Бот": win_bot[-1],
                          "Игрок": win_player[-1]
                          }
            await message.channel.send("Бот - " + str(bot_player["Бот"]) + "\n")
            await message.channel.send("Игрок - " + str(bot_player["Игрок"]) + "\n")
            print("\n\nБот - " + str(bot_player["Бот"]) + "\n")
            print("Игрок - " + str(bot_player["Игрок"]) + "\n")
        if(list1[0] == 'Ножницы'and rand == 'Бумага'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы победили!")
            win_player.append(win_player[-1]+1)
            bot_player = {"Бот": win_bot[-1],
                          "Игрок": win_player[-1]
                          }
            await message.channel.send("Бот - " + str(bot_player["Бот"]) + "\n")
            await message.channel.send("Игрок - " + str(bot_player["Игрок"]) + "\n")
            print("\n\nБот - " + str(bot_player["Бот"]) + "\n")
            print("Игрок - " + str(bot_player["Игрок"]) + "\n")
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
    if message.content.startswith('!Бумага'):
        list1 = []
        list1.append("Бумага")
        print(message.author.mention + "\n" +
              "поставил\n"+list1[0].lower()+".\n\n")
        list2 = ['Бумага', 'Камень', 'Ножницы']
        rand = random.choice(list2)
        if(list1[0] == rand):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Ничья!")
            bot_player = {"Бот": win_bot[-1],
                          "Игрок": win_player[-1]
                          }
            await message.channel.send("Бот - " + str(bot_player["Бот"]) + "\n")
            await message.channel.send("Игрок - " + str(bot_player["Игрок"]) + "\n")
            print("\n\nБот - " + str(bot_player["Бот"]) + "\n")
            print("Игрок - " + str(bot_player["Игрок"]) + "\n")
        if(list1[0] == 'Бумага'and rand == 'Камень'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы победили!")
            win_player.append(win_player[-1]+1)
            bot_player = {"Бот": win_bot[-1],
                          "Игрок": win_player[-1]
                          }
            await message.channel.send("Бот - " + str(bot_player["Бот"]) + "\n")
            await message.channel.send("Игрок - " + str(bot_player["Игрок"]) + "\n")
            print("\n\nБот - " + str(bot_player["Бот"]) + "\n")
            print("Игрок - " + str(bot_player["Игрок"]) + "\n")
        if(list1[0] == 'Камень'and rand == 'Бумага'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы проиграли!")
            win_bot.append(win_bot[-1]+1)
            bot_player = {"Бот": win_bot[-1],
                          "Игрок": win_player[-1]
                          }
            await message.channel.send("Бот - " + str(bot_player["Бот"]) + "\n")
            await message.channel.send("Игрок - " + str(bot_player["Игрок"]) + "\n")
            print("\n\nБот - " + str(bot_player["Бот"]) + "\n")
            print("Игрок - " + str(bot_player["Игрок"]) + "\n")
        if(list1[0] == 'Ножницы'and rand == 'Камень'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы проиграли!")
            win_bot.append(win_bot[-1]+1)
            bot_player = {"Бот": win_bot[-1],
                          "Игрок": win_player[-1]
                          }
            await message.channel.send("Бот - " + str(bot_player["Бот"]) + "\n")
            await message.channel.send("Игрок - " + str(bot_player["Игрок"]) + "\n")
            print("\n\nБот - " + str(bot_player["Бот"]) + "\n")
            print("Игрок - " + str(bot_player["Игрок"]) + "\n")
        if(list1[0] == 'Камень'and rand == 'Ножницы'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы победили!")
            win_player.append(win_player[-1]+1)
            bot_player = {"Бот": win_bot[-1],
                          "Игрок": win_player[-1]
                          }
            await message.channel.send("Бот - " + str(bot_player["Бот"]) + "\n")
            await message.channel.send("Игрок - " + str(bot_player["Игрок"]) + "\n")
            print("\n\nБот - " + str(bot_player["Бот"]) + "\n")
            print("Игрок - " + str(bot_player["Игрок"]) + "\n")
        if(list1[0] == 'Бумага'and rand == 'Ножницы'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы проиграли!")
            win_bot.append(win_bot[-1]+1)
            bot_player = {"Бот": win_bot[-1],
                          "Игрок": win_player[-1]
                          }
            await message.channel.send("Бот - " + str(bot_player["Бот"]) + "\n")
            await message.channel.send("Игрок - " + str(bot_player["Игрок"]) + "\n")
            print("\n\nБот - " + str(bot_player["Бот"]) + "\n")
            print("Игрок - " + str(bot_player["Игрок"]) + "\n")
        if(list1[0] == 'Ножницы'and rand == 'Бумага'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы победили!")
            win_player.append(win_player[-1]+1)
            bot_player = {"Бот": win_bot[-1],
                          "Игрок": win_player[-1]
                          }
            await message.channel.send("Бот - " + str(bot_player["Бот"]) + "\n")
            await message.channel.send("Игрок - " + str(bot_player["Игрок"]) + "\n")
            print("\n\nБот - " + str(bot_player["Бот"]) + "\n")
            print("Игрок - " + str(bot_player["Игрок"]) + "\n")
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
    if message.content.startswith('!Ножницы'):
        list1 = []
        list1.append("Ножницы")
        print(message.author.mention + "\n" +
              "поставил\n"+list1[0].lower()+".\n\n")
        list2 = ['Бумага', 'Камень', 'Ножницы']
        rand = random.choice(list2)
        if(list1[0] == rand):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Ничья!")
            bot_player = {"Бот": win_bot[-1],
                          "Игрок": win_player[-1]
                          }
            await message.channel.send("Бот - " + str(bot_player["Бот"]) + "\n")
            await message.channel.send("Игрок - " + str(bot_player["Игрок"]) + "\n")
            print("\n\nБот - " + str(bot_player["Бот"]) + "\n")
            print("Игрок - " + str(bot_player["Игрок"]) + "\n")
        if(list1[0] == 'Бумага'and rand == 'Камень'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы победили!")
            win_player.append(win_player[-1]+1)
            bot_player = {"Бот": win_bot[-1],
                          "Игрок": win_player[-1]
                          }
            await message.channel.send("Бот - " + str(bot_player["Бот"]) + "\n")
            await message.channel.send("Игрок - " + str(bot_player["Игрок"]) + "\n")
            print("\n\nБот - " + str(bot_player["Бот"]) + "\n")
            print("Игрок - " + str(bot_player["Игрок"]) + "\n")
        if(list1[0] == 'Камень'and rand == 'Бумага'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы проиграли!")
            win_bot.append(win_bot[-1]+1)
            bot_player = {"Бот": win_bot[-1],
                          "Игрок": win_player[-1]
                          }
            await message.channel.send("Бот - " + str(bot_player["Бот"]) + "\n")
            await message.channel.send("Игрок - " + str(bot_player["Игрок"]) + "\n")
            print("\n\nБот - " + str(bot_player["Бот"]) + "\n")
            print("Игрок - " + str(bot_player["Игрок"]) + "\n")
        if(list1[0] == 'Ножницы'and rand == 'Камень'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы проиграли!")
            win_bot.append(win_bot[-1]+1)
            bot_player = {"Бот": win_bot[-1],
                          "Игрок": win_player[-1]
                          }
            await message.channel.send("Бот - " + str(bot_player["Бот"]) + "\n")
            await message.channel.send("Игрок - " + str(bot_player["Игрок"]) + "\n")
            print("\n\nБот - " + str(bot_player["Бот"]) + "\n")
            print("Игрок - " + str(bot_player["Игрок"]) + "\n")
        if(list1[0] == 'Камень'and rand == 'Ножницы'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы победили!")
            win_player.append(win_player[-1]+1)
            bot_player = {"Бот": win_bot[-1],
                          "Игрок": win_player[-1]
                          }
            await message.channel.send("Бот - " + str(bot_player["Бот"]) + "\n")
            await message.channel.send("Игрок - " + str(bot_player["Игрок"]) + "\n")
            print("\n\nБот - " + str(bot_player["Бот"]) + "\n")
            print("Игрок - " + str(bot_player["Игрок"]) + "\n")
        if(list1[0] == 'Бумага'and rand == 'Ножницы'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы проиграли!")
            win_bot.append(win_bot[-1]+1)
            bot_player = {"Бот": win_bot[-1],
                          "Игрок": win_player[-1]
                          }
            await message.channel.send("Бот - " + str(bot_player["Бот"]) + "\n")
            await message.channel.send("Игрок - " + str(bot_player["Игрок"]) + "\n")
            print("\n\nБот - " + str(bot_player["Бот"]) + "\n")
            print("Игрок - " + str(bot_player["Игрок"]) + "\n")
        if(list1[0] == 'Ножницы'and rand == 'Бумага'):
            await message.channel.send("Бот поставил  " + rand.lower()+".")
            await message.channel.send("Вы победили!")
            win_player.append(win_player[-1]+1)
            bot_player = {"Бот": win_bot[-1],
                          "Игрок": win_player[-1]
                          }
            await message.channel.send("Бот - " + str(bot_player["Бот"]) + "\n")
            await message.channel.send("Игрок - " + str(bot_player["Игрок"]) + "\n")
            print("\n\nБот - " + str(bot_player["Бот"]) + "\n")
            print("Игрок - " + str(bot_player["Игрок"]) + "\n")
    if message.content.startswith('!leave'):
        await message.channel.send(second_comand[0]+'\n'+second_comand[1]+'\n'+second_comand[2])
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run(TOKEN)


def check_win(answer1 )