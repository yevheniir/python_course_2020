import telebot

bot = telebot.TeleBot('1128710448:AAERRXGH2X-93HYJpQx5qYJ9unNG47lLbUQ')
    
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text[0].lower() == "н" and check_all(message.text[1:].lower(), "a"):
        bot.send_message(message.chat.id, message.text + message.text[1:] )

bot.polling()

def check_all(string, later):
    for l in string:
       if l != later:
           return False 