import telebot

token = str('5649650835:AAETquP7oY4XjskPkSVtfRNQimAmnZ6OdZ0')
bot=telebot.TeleBot(token)
id = set()
command_list = ['start']


@bot.message_handler(commands=command_list)
def command_issue(message):
    id.append(message.chat.id)

print(id)
bot.infinity_polling(timeout=10)
