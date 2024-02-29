import telebot
import query
from config import TOKEN


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Привет! Добро пожаловать в бота сбора обратной связи!')


@bot.message_handler(commands=['authorize'])
def authorize(message):
    chat_id = message.chat.id
    if query.auth(chat_id):
        bot.send_message(chat_id, 'Вы авторизированы в боте!')
    else:
        bot.send_message(chat_id, 'У Вас нет доступа :(')


def new_request():
    chat_id = query.get_ids()
    print(chat_id)

    for id in chat_id:
        print()
        chat_id = str(id)[1:-2]
        bot.send_message(int(chat_id), 'Получена новая заяка!')


def start():
    print('Бот запущен!')
    bot.polling()
