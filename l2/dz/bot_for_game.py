import discord
import random
import time
message = '!play' or '!notplay' or '!yes' or '!no' or '!1' or '!2' or '!3'
message_1 = '!play' or '!notplay'
message_for_start = '!yes' or '!no'
ваш_вибір = '!1' or '!2' or '!3'

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        if('!play'):
            await message.channel.send('Вітаю у грі камінь ножиці бумага.Правила такі:щоб відкрити гру введіть !play, відповідати на запитання можна використовуючи відповіді !yes і !no, для вибору предмета 1-камінь, 2-ножиці, 3-бумага')
            time.sleep(2)
            await message.chanel.send('Бажаєте зіграти?(!yes або !no)')
            if('!yes'):
                print('Чудово.Ваш предмет?(1-камінь, 2-ножиці, 3-бумашга)')
                камінь = 1
                ножиці = 2
                бумага = 3
                камінь>ножиці
                ножиці>бумага
                бумага>камінь
                вибір_бота = random(1,3)
                if ваш_вибір>вибір_бота:
                    print('Ви виграли!))))')
                if ваш_вибір<вибір_бота:
                    print('Ви програли.((((')
            else:
                print('Шкода.Я так хотів зіграти.((((')
                time.sleep(9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)




client = MyClient()
client.run('NzIyMTEwNzQ2Nzc4OTI3Mjg1.XuyEng.4pTMMFTLe1NjrzKJuOpgZE4DFzw')