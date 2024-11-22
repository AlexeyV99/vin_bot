from telebot import TeleBot, types
import time

from config_data.config import DEFAULT_COMMANDS
from loader import bot, logger
from handlers import default_handlers, admin, vin


def main():
    while True:
        try:

            default_handlers.register_default_handlers(bot)
            admin.register_admin_handlers(bot)
            vin.register_vin_handlers(bot)

            logger.info(f'== Бот запущен ==')
            bot.set_my_commands(
                commands=[types.BotCommand(*i) for i in DEFAULT_COMMANDS]
            )
            bot.polling(none_stop=True)

        except Exception as ex:
            logger.error(f'Ошибка:\n{ex}')
            time.sleep(2)


if __name__ == "__main__":
   main()
