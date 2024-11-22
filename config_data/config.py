import os
from dotenv import load_dotenv, find_dotenv


if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

# описываем глобальные переменные
BOT_TOKEN: str = os.getenv('BOT_TOKEN')

# команды по умолчанию
DEFAULT_COMMANDS: tuple = (
    ('start', "Запустить бота"),
    ('admin', "Написать админу"),
    ('vin', "Проверить ВИН"),
    ('info', 'Данные пользователя')
)

# файл базы данных
DB_NAME: str = 'bot_base.db'

#  Введите ID чатов админов через символ '/'
ADMIN_CHAT = '750109032/'
