import telebot

bot = telebot.TeleBot('1128710448:AAERRXGH2X-93HYJpQx5qYJ9unNG47lLbUQ')

def check_all(string, later):
    for l in string:
       if l != later:
           print("NO")
           return False 
    return True
    
@bot.message_handler(content_types=['text'])
def send_text(message):
    print(message.text)
    print(message.text[0].lower() == "н")
    print(check_all(message.text[1:].lower(), "а"))
    if message.text[0].lower() == "н" and check_all(message.text[1:].lower(), "а"):
        message_result = message.text + message.text[1:]
        if len(message.text) >= 4096:
            print()
            message_result = message_result[:4096]
        bot.send_message(message.chat.id, message_result)

bot.polling()

