from config_data.config import DEFAULT_COMMANDS, BOT_TOKEN
from telebot import TeleBot
import logging
from logging import config
from logging_config import dict_config


# async def setup_bot_commands(_) -> None:
#     """
#     Загрузка в бот команд по умолчанию
#     :param _:
#     :return:
#     """
#     await bot.set_my_commands([BotCommand(*i) for i in DEFAULT_COMMANDS])
#     logger.info('Бот запущен!')


bot = TeleBot(token=BOT_TOKEN)


config.dictConfig(dict_config)
logger = logging.getLogger(__name__)