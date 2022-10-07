import telebot

token = str('5649650835:AAETquP7oY4XjskPkSVtfRNQimAmnZ6OdZ0')
bot=telebot.TeleBot(token)
id = [976772261]
command_list = ['start']
for i in id:
    bot.send_message(i, 'Tests failed')
