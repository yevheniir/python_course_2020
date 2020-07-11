import telebot

bot = telebot.TeleBot('1128710448:AAERRXGH2X-93HYJpQx5qYJ9unNG47lLbUQ')

def check_all(string, later):
    for l in string:
       if l != later:
           print("NO")
           return False 
    
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text[0].lower() == "н" and check_all(message.text[1:].lower(), "a"):
        pr
        bot.send_message(message.chat.id, message.text + message.text[1:] )

bot.polling()

