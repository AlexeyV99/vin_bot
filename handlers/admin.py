from loader import bot, logger
from telebot import types

from config_data.config import ADMIN_CHAT
# from main import logger


def admin_handler(message) -> None:
    logger.info(f'Пользователь {message.from_user.first_name} (id:{message.from_user.id}) выполнил команду <admin>')
    if str(message.from_user.id) in ADMIN_CHAT:
        rep = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton('Добавить', callback_data='add_ad')
        button2 = types.InlineKeyboardButton('Удалить', callback_data='dell_ad')
        rep.add(button1, button2)
        admins = ''
        for ad in ADMIN_CHAT.split('/'):
            if ad:
                admins += f'\nid: {ad}'
        welcome_text = (f'Список админов:{admins}')
        bot.send_message(message.chat.id, welcome_text, reply_markup=rep)
    else:
        welcome_text = ("Напишите сообщение админу:")
        bot.register_next_step_handler(message, send_admin_message)
        bot.send_message(message.chat.id, welcome_text)


def send_admin_message(message):
    if not str(message.from_user.id) in ADMIN_CHAT:
        bot.reply_to(message, "Сообщение отправлено администратору")
        logger.info(
            f'Пользователь {message.from_user.first_name} (id:{message.from_user.id}) отправил сообщение админу')
        for admin in ADMIN_CHAT.split('/'):
            if admin:
                rep = types.InlineKeyboardMarkup(row_width=2)
                button1 = types.InlineKeyboardButton('Ответить', callback_data=str(message.chat.id))
                button2 = types.InlineKeyboardButton('Удалить', callback_data='dell')
                rep.add(button1, button2)
                bot.send_message(admin, f'Сообщение: \n*********** \n{message.text}\n*********** \n'
                                        f'Пользователь: @{message.from_user.first_name} ('
                                        f'id:{message.from_user.id})',
                                 reply_markup=rep)

@bot.callback_query_handler(func=lambda callback: True)
def callback_inline(call):
    if call.message:

        if call.data == "dell":
            bot.delete_message(call.message.chat.id, call.message.id)
        elif call.data == 'add_ad':
            msg = bot.send_message(call.message.chat.id, f'Введите id:')
            bot.register_next_step_handler(msg, admin_add)
        elif call.data == 'dell_ad':
            msg = bot.send_message(call.message.chat.id, f'Введите id:')
            bot.register_next_step_handler(msg, admin_dell)
        else:
            msg = bot.send_message(call.message.chat.id, f'Введите ответ для {call.message.from_user.first_name}:')
            bot.register_next_step_handler(msg, answer, call.data, call.from_user.username)
            bot.delete_message(call.message.chat.id, call.message.id)


def answer(message, data, name):
    bot.delete_message(message.chat.id, message.id)
    logger.info(f'Ответ от администратора отправлен пользователю {name}')
    bot.send_message(data, f"Ответ от админа:\n***********\n{message.text}")
    bot.send_message(message.chat.id, f'Ответ отправлен пользователю {name}')


def admin_add(message):
    if message.text.isdigit():
        global ADMIN_CHAT
        logger.info(f'Пользователь {message.text} добавлен к администраторам')
        ADMIN_CHAT += f'{message.text}/'
        bot.send_message(message.chat.id, f'Пользователь {message.text} добавлен к администраторам')
    else:
        bot.send_message(message.chat.id, f'Ошибка ввода id')


def admin_dell(message):
    if message.text.isdigit():
        global ADMIN_CHAT
        if message.text in ADMIN_CHAT:
            new_admin = ADMIN_CHAT.replace(f'{message.text}/', '')
            logger.info(f'Пользователь {message.text} удален из администраторов')
            bot.send_message(message.chat.id, f'Пользователь {message.text} удален из администраторов')
            ADMIN_CHAT = new_admin
        else:
            bot.send_message(message.chat.id, f'Такого админа нет!')
    else:
        bot.send_message(message.chat.id, f'Ошибка ввода id')


def register_admin_handlers(bot) -> None:
    bot.register_message_handler(admin_handler, commands=['admin'])


