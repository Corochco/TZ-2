import telebot

token = str('5649650835:AAETquP7oY4XjskPkSVtfRNQimAmnZ6OdZ0')
bot=telebot.TeleBot(token)
with open('id.txt') as f:
    id = list(map(int, f.readline().split()))

for i in id:
    bot.send_message(i, 'Tests passed')
