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
    try:
        chat_id = message.chat.id
        bot.send_message(chat_id, 'Привет! Добро пожаловать в бота сбора обратной связи!')
    except Exception as error:
        bot.send_message(chat_id, 'Произошла ошибка: ' + str(error) + '\nПопробуйте снова')


@bot.message_handler(commands=['get_all'])
def get_all(message):
    try:
        if authorize(message):
            chat_id = message.chat.id
            res = query.out_all_id()
            for id in res:
                result = query.out(f"""SELECT name, phone, city, company, status, comment FROM contacts WHERE id='{id[0]}'""")
                result_string = f'ID: {id[0]}\nИмя: {result[0][0]}\nТелефон: {result[0][1]}\nГород: {result[0][2]}\nЗастройщик/компания: {result[0][3]}\nСтатус: {result[0][4]}\nКомментарий: {result[0][5]}'
                bot.send_message(chat_id, result_string)
    except Exception as error:
        bot.send_message(chat_id, 'Произошла ошибка: ' + str(error) + '\nПопробуйте снова')


@bot.message_handler(commands=['get_all_open'])
def get_all_open(message):
    try:
        if authorize(message):
            chat_id = message.chat.id
            res = query.out_all_open()
            if len(res) > 0:
                for id in res:
                    result = query.out(f"""SELECT name, phone, city, company, status, comment FROM contacts WHERE id={id[0]}""")
                    result_string = f'ID: {id[0]}\nИмя: {result[0][0]}\nТелефон: {result[0][1]}\nГород: {result[0][2]}\nЗастройщик/компания: {result[0][3]}\nСтатус: {result[0][4]}\nКомментарий: {result[0][5]}'
                    bot.send_message(chat_id, result_string)
            else:
                bot.send_message(chat_id, 'Нет открытых заявок')
    except Exception as error:
        bot.send_message(chat_id, 'Произошла ошибка: ' + str(error) + '\nПопробуйте снова')


@bot.message_handler(commands=['get_request'], content_types=['text'])
def enter_id(message):
    try:
        if authorize(message):
            chat_id = message.chat.id
            bot.send_message(chat_id, 'Введите ID заявки, чтобы посмотреть её')
            bot.register_next_step_handler(message, get_request)
    except Exception as error:
        bot.send_message(chat_id, 'Произошла ошибка: ' + str(error) + '\nПопробуйте снова')


def get_request(message):
    try:
        if authorize(message):
            chat_id = message.chat.id
            entered_id = message.text
            if entered_id != None and int(entered_id) <= query.out(f"""SELECT id FROM contacts ORDER BY id DESC LIMIT 1""")[0][0]:
                result = query.out(f"""SELECT name, phone, city, company, status, comment FROM contacts WHERE id='{entered_id}'""")
                result_string = f'ID: {entered_id}\nИмя: {result[0][0]}\nТелефон: {result[0][1]}\nГород: {result[0][2]}\nЗастройщик/компания: {result[0][3]}\nСтатус: {result[0][4]}\nКомментарий: {result[0][5]}'
                bot.send_message(chat_id, result_string)
            else:
                bot.send_message(chat_id, 'Введен неверный ID заявки')
    except Exception as error:
        bot.send_message(chat_id, 'Произошла ошибка: ' + str(error) + '\nПопробуйте снова')


@bot.message_handler(commands=['edit_status'], content_types=['text'])
def enter_id_status(message):
    try:
        if authorize(message):
            chat_id = message.chat.id
            bot.send_message(chat_id, 'Введите ID заявки, чтобы изменить её статус')
            bot.register_next_step_handler(message, enter_status)
    except Exception as error:
        bot.send_message(chat_id, 'Произошла ошибка: ' + str(error) + '\nПопробуйте снова')


def enter_status(message):
    try:
        if authorize(message):
            global auth_id_status
            chat_id = message.chat.id
            bot.send_message(chat_id, 'Введите новый статус')
            auth_id_status = int(message.text)
            bot.register_next_step_handler(message, edit_status)
    except Exception as error:
        bot.send_message(chat_id, 'Произошла ошибка: ' + str(error) + '\nПопробуйте снова')


def edit_status(message):
    try:
        if authorize(message):
            chat_id = message.chat.id
            entered_status = message.text
            if entered_status != None:
                query.insert(f"""UPDATE contacts SET status='{entered_status}' WHERE id='{auth_id_status}'""")
                bot.send_message(chat_id, f'Статус успешно изменён на {entered_status}')
            else:
                bot.send_message(chat_id, 'Введен неверный ID заявки')
    except Exception as error:
        bot.send_message(chat_id, 'Произошла ошибка: ' + str(error) + '\nПопробуйте снова')


@bot.message_handler(commands=['edit_comment'], content_types=['text'])
def enter_id_comment(message):
    try:
        if authorize(message):
            chat_id = message.chat.id
            bot.send_message(chat_id, 'Введите ID заявки, чтобы изменить её комментарий')
            bot.register_next_step_handler(message, enter_comment)
    except Exception as error:
        bot.send_message(chat_id, 'Произошла ошибка: ' + str(error) + '\nПопробуйте снова')


def enter_comment(message):
    try:
        if authorize(message):
            global auth_id_comment
            chat_id = message.chat.id
            bot.send_message(chat_id, 'Введите новый комментарий')
            auth_id_comment = int(message.text)
            bot.register_next_step_handler(message, edit_comment)
    except Exception as error:
        bot.send_message(chat_id, 'Произошла ошибка: ' + str(error) + '\nПопробуйте снова')


def edit_comment(message):
    try:
        if authorize(message):
            chat_id = message.chat.id
            entered_comment = message.text
            if entered_comment != None:
                query.insert(f"""UPDATE contacts SET comment='{entered_comment}' WHERE id='{auth_id_comment}'""")
                bot.send_message(chat_id, f'Комментарий успешно изменён на {entered_comment}')
            else:
                bot.send_message(chat_id, 'Введен неверный ID заявки')
    except Exception as error:
        bot.send_message(chat_id, 'Произошла ошибка: ' + str(error) + '\nПопробуйте снова')


def new_request(id):
    try:
        chat_id = query.get_ids()
        result = query.out(f"""SELECT name, phone, city, company, status, comment FROM contacts WHERE id='{id}'""")
        result_string = f'ID: {id}\nИмя: {result[0][0]}\nТелефон: {result[0][1]}\nГород: {result[0][2]}\nЗастройщик/компания: {result[0][3]}\nСтатус: {result[0][4]}\nКомментарий: {result[0][5]}'
        for id in chat_id:
            chat_id = str(id)[1:-2]
            bot.send_message(chat_id, 'Получена новая заяка!\n' + result_string)
    except Exception as error:
        bot.send_message(chat_id, 'Произошла ошибка: ' + str(error) + '\nПопробуйте снова')


def start():
    print('Бот запущен!')
    bot.polling(none_stop=True)
