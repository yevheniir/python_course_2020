import telebot

bot = telebot.TeleBot('776550937:AAELEr0c3H6dM-9QnlDD-0Q0Fcd65pPyAiM')
    
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, )
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')

bot.polling()