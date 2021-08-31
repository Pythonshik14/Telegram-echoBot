import telebot

bot = telebot.TeleBot("1829844096:AAEQQ_bS2flfLfuWYEJ_NuxO4-7ozTVo13M")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()