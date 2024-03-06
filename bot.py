import telebot
import query
from config import TOKEN


bot = telebot.TeleBot(TOKEN)


def authorize(message):
    chat_id = message.chat.id
    if query.auth(chat_id):
        return True
    else:
        bot.send_message(chat_id, 'У Вас нет доступа :(')
        return False


@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Привет! Добро пожаловать в бота сбора обратной связи!')


@bot.message_handler(commands=['get_all'])
def get_all(message):
    if authorize(message):
        chat_id = message.chat.id
        res = query.out_all_id()
        for id in res:
            result = query.out(f"""SELECT name, phone, city, company, status, comment FROM contacts WHERE id='{id[0]}'""")
            result_string = f'ID: {id[0]}\nИмя: {result[0][0]}\nТелефон: {result[0][1]}\nГород: {result[0][2]}\nЗастройщик/компания: {result[0][3]}\nСтатус: {result[0][4]}\nКомментарий: {result[0][5]}'
            bot.send_message(chat_id, result_string)


@bot.message_handler(commands=['get_request'], content_types=['text'])
def enter_id(message):
    if authorize(message):
        chat_id = message.chat.id
        bot.send_message(chat_id, 'Введите ID заявки, чтобы посмотреть её')
        bot.register_next_step_handler(message, get_request)


def get_request(message):
    if authorize(message):
        chat_id = message.chat.id
        entered_id = message.text
        if entered_id != None and int(entered_id) <= query.out(f"""SELECT id FROM contacts ORDER BY id DESC LIMIT 1""")[0][0]:
            result = query.out(f"""SELECT name, phone, city, company, status, comment FROM contacts WHERE id='{entered_id}'""")
            result_string = f'ID: {entered_id}\nИмя: {result[0][0]}\nТелефон: {result[0][1]}\nГород: {result[0][2]}\nЗастройщик/компания: {result[0][3]}\nСтатус: {result[0][4]}\nКомментарий: {result[0][5]}'
            bot.send_message(chat_id, result_string)
        else:
            bot.send_message(chat_id, 'Введен неверный ID заявки')


@bot.message_handler(commands=['edit_status'], content_types=['text'])
def enter_id(message):
    if authorize(message):
        chat_id = message.chat.id
        bot.send_message(chat_id, 'Введите ID заявки, чтобы изменить её статус')
        bot.register_next_step_handler(message, enter_status)


def enter_status(message):
    if authorize(message):
        global id
        chat_id = message.chat.id
        bot.send_message(chat_id, 'Введите новый статус')
        id = message.text
        bot.register_next_step_handler(message, edit_status)


def edit_status(message):
    if authorize(message):
        chat_id = message.chat.id
        entered_status = message.text
        if entered_status != None:
            query.insert(f"""UPDATE contacts SET status='{entered_status}' WHERE id='{id}'""")
            bot.send_message(chat_id, f'Статус успешно изменён на {entered_status}')
        else:
            bot.send_message(chat_id, 'Введен неверный ID заявки')


def new_request():
    chat_id = query.get_ids()

    for id in chat_id:
        chat_id = str(id)[1:-2]
        bot.send_message(int(chat_id), 'Получена новая заяка!')


def start():
    print('Бот запущен!')
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as error:
            print(error)
