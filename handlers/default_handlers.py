from typing import Union
# from aiogram.types import Message, CallbackQuery
from loader import bot, logger
from telebot import types
# from keyboards.inline_kb import inline_keyboard_help, inline_keyboard_default
# from handlers.func import delete_message

from config_data.config import ADMIN_CHAT


def bot_start(message: Union[types.Message, types.CallbackQuery]) -> None:
    logger.info(f'Пользователь {message.from_user.first_name} (id:{message.from_user.id}) выполнил команду <start>')
    commands = ''
    if str(message.from_user.id) in ADMIN_CHAT:
        welcome_text = ("Вы - АДМИНИСТРАТОР!")
    else:
        welcome_text = ("Вы - ПОЛЬЗОВАТЕЛЬ!")
    bot.send_message(message.chat.id, f'"Привет! Это информационный бот !\n{welcome_text}{commands}')


def user_info(message):
    logger.info(f'Пользователь {message.from_user.first_name} (id:{message.from_user.id}) выполнил команду <info>')
    if str(message.from_user.id) in ADMIN_CHAT:
        welcome_text = ("Вы являетесь АДМИНИСТРАТОРОМ!")
    else:
        welcome_text = ("Вы являетесь ПОЛЬЗОВАТЕЛЕМ!")
    info = welcome_text + (f'\nid: {message.from_user.id}'
                           f'\nname: {message.from_user.first_name}'
                           f'\nlast_name: {message.from_user.last_name}'
                           f'\nuser_name: {message.from_user.username}'
                           f'\nbot: {message.from_user.is_bot}'
                           f'\nlanguage_code: {message.from_user.language_code}')
    bot.send_message(message.chat.id, info)


# async def bot_help(message: Union[Message, CallbackQuery]) -> None:
#     await delete_message(message)
#     logger.info(f'Пользователь {message.from_user.full_name}({message.from_user.id}) выполнил команду "help"')
#     await bot.send_message(message.from_user.id, f"Команды бота:\n", parse_mode='html',
#                            reply_markup=inline_keyboard_default())
#



def register_default_handlers(bot) -> None:
    bot.register_message_handler(bot_start, commands=['start'])
    bot.register_message_handler(user_info, commands=['info'])


