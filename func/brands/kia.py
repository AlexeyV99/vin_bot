# Z94C241BBKR086973

from func.data.f_year import rez_num_10
from loader import logger


factory = {
    'CGK': 'Марокко',
    'LJD': 'Китай',
    'TMA': 'Чехия',
    'XWW': 'Казахстан',
    'X4X': 'Россия',
    '5XX': 'США'
    }
    
model= {
    'DA': 'Pride',
    '5P': 'Pride',
    'BE': 'Picanto I',
    'BX': 'Picanto I',
    'BJ': 'Picanto II',
    'CB': 'Rio III',
    'CC': 'Rio III',
    'CE': 'Retona',
    'DB': 'Abela/Avella',
    'DC': 'Rio I',
    'DE': 'Rio II',
    'DG': 'Rio II',
    'DT': 'Pride Van',
    'DJ': 'Rio',
    'EG': 'Venga',
    'EH': 'Venga',
    'EK': 'Venga',
    'FA': 'Sephia (4WD)',
    'FB': 'Sephia',
    'FC': 'Carens (minivan)',
    'FD': 'Carens',
    'FF': 'C`eed I',
    'FH': 'Cerato',
    'FP': 'Carens 5 Van',
    'FT': 'Cerato',
    'FU': 'Cerato',
    'FW': 'Cerato',
    'GA': 'Concord',
    'GB': 'Capital',
    'GC': 'Claris/Credos',
    'GD': 'Optima',
    'GE': 'Magentis III',
    'GM': 'Optima III',
    'GN': 'Optima III',
    'HB': 'C`eed I',
    'HC': 'C`eed I',
    'HH': 'Carens II',
    'HN': 'C`eed II',
    'HM': 'C`eed II',
    'JG': 'Soul',
    'JT': 'Soul',
    'JA': 'Sportage I',
    'JB': 'Sportage I',
    'JC': 'Sorento I',
    'JE': 'Sportage II',
    'KH': 'Sportage III',
    'KN': 'Mohave',
    'KU': 'Sorento II',
    'LA': 'Potentia',
    'LB': 'Enterprise',
    'LC': 'Enterprise Limousine',
    'LD': 'Opirus',
    'MA': 'Makival/Carnival',
    'MH': 'Carnival III',
    'PB': 'Sportage III',
    'PC': 'Sportage III',
    'RA': 'Sportage (cargo)',
    'SA': 'Bongo Frontier (cargo)',
    'SB': 'Bongo Ceres (cargo)',
    'SC': 'Wide Bongo (cargo)',
    'SP': 'Bongo (bus)',
    'SR': 'Bongo Town (bus)',
    'TA': 'Besta (cargo)',
    'TB': 'Pregio (cargo)',
    'TP': 'Besta (bus)',
    'TR': 'Pregio (bus)',
    'UA': 'Carnival (cargo)',
    'UP': 'Carnival (minivan)',
    'WA': 'Super Titan (cargo)',
    'WB': 'Jimbo Titan (cargo)',
    'WC': 'Titan Pride (cargo)',
    'WD': 'Titan (cargo, 1.25 t)',
    'WX': 'Joice'
    
    }

body ={
    '21': 'двухдверный седан',
    '22': 'четырехдверный седан',
    '23': 'трехдверный хэтчбэк',
    '24': 'пятидверный хэтчбэк',
    '31': 'двухдверный купе',
    '32': 'четырехдверный купе',
    '33': 'трехдверный хэтчбэк',
    '34': 'пятидверный хэтчбэк',
    '35': 'двухдверный',
    '41': 'двухдверный седан',
    '42': 'четырехдверный седан',
    '43': 'трехдверный',
    '44': 'пятидверный',
    '45': 'двухдверный',
    '46': 'четырехдверный',
    '47': 'двухдверный',
    '48': 'двухдверный tarpaulin',
    '49': 'четырехдверный tarpaulin',
    '51': 'трехдверный универсал',
    '52': 'пятидверный универсал',
    '53': 'двухдверный SUV (plastic top)',
    '54': 'двухдверный SUV (awning)',
    '55': 'четырехдверный SUV',
    '61': 'трехдверный комби',
    '62': 'пятидверный комби',
    '63': 'двухдверный пикап',
    '71': 'четырехдверный MPV',
    '72': 'четырехдверный MPV (high roof)',
    '73': 'четырехдверный MPV',
    '74': 'четырехдверный (high roof)',
    '75': 'пятидверный',
    '81': 'четырехдверный',
    '82': 'четырехдверный (high roof)',
    '83': 'четырехдверный',
    '84': 'четырехдверный (high roof)',
    '85': 'пятидверный'
}

engine = {
    'C`eed I': {
        '1': '1396 мл. / 109 л.с.',
        '2': '1591 мл. / 122 (124) л.с.',
        '3': '1975 мл. / 142 л.с.',
        '4': '1582 мл. / 115 л.с.',
        '6': '1591 мл. / 122 л.с.'
    },
    'C`eed II': {
        '2': '1582 мл. / 103 л.с.',
        '6': '1582 мл. / 115 л.с.'
    },
    'Cerato': {
        '1': '1591 мл. / 126 л.с.',
        '2': '1998 мл. / 164 л.с.',
        '3': '1591 мл. / 126 л.с.'
    },
    'Rio I': {
        '1': '1343 мл. / 84 л.с.',
        '2': '1493 мл. / 95 л.с.',
        '3': '1493 мл. / 108 л.с.'
    },
    'Rio II': {
        '1': '1396 мл. / 109 л.с.',
        '4': '1493 мл. / 110 л.с.'
    },
    'Rio III': {
        'A': '1396 мл. / 110 л.с.',
        'B': '1591 мл. / 122 (126) л.с.'
    },
    'Mohave': {
        '1': '3778 мл. / 274 л.с.',
        '3': '2959 мл. / 250 л.с.',
        '4': '2959 мл. / 250 л.с.'
    },
    'Optima': {
        '1': '1836 мл. / 134 л.с.',
        '2': '1997 мл. / 149 л.с.',
        '3': '1997 мл. / 95 л.с.',
        '4': '2493 мл. V6 / 176 л.с.',
        '5': '2 л.',
        '6': '2,4 л.',
        '7': '2,5 л. V6',
        '8': '2,7 л. V6',
        '9': '1975 мл.',
        'A': '1.8 л'
    },
    'Optima III': {
        '1': '1998 мл. / 164 л.с.',
        '2': '2359 мл. / 200 л.с.',
        '4': '1685 мл. / 115 л.с.'
    },
    'Picanto I': {
        '3': '1086 мл. / 65 л.с.'
    },
    'Picanto II': {
        '2': '1248 мл. / 85 л.с.',
        '5': '998 мл. / 69 л.с.'
    },
    'Sorento': {
        '1': '2.5 л. / 140 л.с.',
        '2': '2.4 л.',
        '3': '3.5 л. V6'
    },
    'Sorento II': {
        '1': '2349 мл. / 174 л.с.',
        '4': '2497 мл. / 170 л.с.'
    },
    'Soul': {
        '1': '1591 мл. / 124 л.с.',
        '2': '1591 мл. / 122 л.с.',
        '3': '1582 мл. / 115 л.с.',
    },
    'Sportage': {
        '1': '1998 мл. / 99 л.с.',
        '2': '1998 мл. / 99 (97) л.с.',
        '3': '1998 мл. / 139 (136) л.с.',
        '4': '2184 мл. / 70 л.с.',
        '5': '1998 мл. / 65 л.с.',
        '6': '1998 мл. / 91 (87) л.с.',
        '7': '1998 мл. / 93 (90) л.с.',
        '8': '1998 мл. / 139 л.с.',
        '9': 'CNG'
    },
    'Sportage II': {
        '1': '1991 мл. / 150 л.с.',
        '2': '1975 мл. / 142 л.с.'
    },
    'Sportage III': {
        '1': '1991 мл. / 150 л.с.',
        '2': '1975 мл. / 142 л.с.'
    },
}

trans = {
    '1': 'пятиступенчатая механика',
    '2': 'трехступенчатый автомат',
    '3': 'четырехступенчатый автомат',
    '5': 'пятиступенчатая механика',
    '9': 'CVT',
}


assembly = {
    '5': 'Hwa-Sung, Korea',
    '6': 'Sohari, Korea',
    '7': 'Korea',
    'A': 'Hwa-Sung, Korea',
    'D': 'Karmann, Deutschland',
    'J': 'Ostrava Hrabova, Czech Republic',
    'L': 'Zilina, Slovakia',
    'R': 'St.Petersburg, Russia',
    'S': 'Shari, Korea',
    'T': 'Korea'
}

def info_kia(message, vin):
    logger.info(f'Пользователь {message.from_user.first_name} (id:{message.from_user.id}) выполнил команду {__name__}')
    info = {}
    result = "<b>== ПОДРОБНАЯ ИНФОРМАЦИЯ ПО KIA ==</b>\n"
    if factory.get(vin[:3]):
        info['Производство'] = factory.get(vin[:3])
        
    model_car = model.get(vin[3:5])
    
    if model_car:
        info['Модель'] = model_car
    if body.get(vin[5:7]):
        info['Кузов'] = body.get(vin[5:7])
    if engine.get(model_car):
        if engine.get(model_car).get(vin[7]):
            info['Мощность двигателя'] = engine.get(model_car).get(vin[7])
    if trans.get(vin[8]):
        info['Коробка передач'] = trans.get(vin[8])
    # Модельный год
    rez_num_10(info, vin)
    
    if assembly.get(vin[10]):
        info['Сборка'] = assembly.get(vin[10])
    info['Серийный номер'] = vin[-6:]
    
    for i_key, i_value in info.items():
        result += f'{i_key}: {i_value}\n'    
    
    return result
