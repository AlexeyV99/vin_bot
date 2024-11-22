from vininfo import Vin
from loader import logger


def vin_info_search(message, vin):
    logger.info(f'Пользователь {message.from_user.first_name} (id:{message.from_user.id}) выполнил команду {__name__}')
    try:
        vin_numbr = Vin(vin)
        return f'<b>== Информация от VININFO ==</b>\n'\
                f'Страна: <i>{vin_numbr.country}</i>\n'\
                f'Производитель: <i>{vin_numbr.manufacturer}</i>\n'\
                f'Модель: <i>{vin_numbr.wmi}</i>\n'\
                f'Тип ТС: <i>{vin_numbr.vds}</i>\n'\
                f'Серийный номер: <i>{vin_numbr.vis}</i>\n'\
                f'Регион: <i>{vin_numbr.region}</i>'
    except Exception as ex:

        logger.error(f'!Ошибка проверки ВИН {vin}\n{ex}')
        return 'Ошибка проверки ВИН в модуле Vininfo'
