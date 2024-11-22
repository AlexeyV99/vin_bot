from func.data.f_region import rez_region
from func.data.f_country import rez_num_1
from func.data.f_factory import rez_wim
from func.data.f_factory_rus import rez_wim_rus
from func.data.f_brand import rez_num_2
from func.data.f_year import rez_num_10
from func.data.f_add import rez_rare
from func.data.f_CRC import rez_crc
from loader import logger




def my_vin_search(message, vin):
    logger.info(f'Пользователь {message.from_user.first_name} (id:{message.from_user.id}) выполнил команду {__name__}')

    info = {}
    result = "<b>== МОИ ДАННЫЕ ==</b>\n"

    #Регион
    rez_region(info, vin)
    #Страна
    rez_num_1(info, vin)
    #Завод
    rez_wim(info, vin)
    #Завод в России
    rez_wim_rus(info, vin)
    #Марка ТС
    # rez_num_2(info, vin)
    # Модельный год
    rez_num_10(info, vin)
    #Дополнительная информация
    rez_rare(info, vin)
    # Проверка контрольной суммы
    rez_crc(info, vin)
    
    info['Модель (WMI)'] = vin[:3]
    info['Тип ТС (VDS)'] = vin[3:9]
    info['Серийный номер (VIS)'] = vin[9:]
    
    for i_key, i_value in info.items():
        result += f'{i_key}: <i>{i_value}</i>\n'
    
    return result
