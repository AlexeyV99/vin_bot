import os


def rez_wim_rus(info, vin):
    result = ''
    rez_path = os.path.join(os.getcwd(), 'func/data', 'WMI_RUS.txt')
    with open(rez_path, 'r') as file:
        for i_line in file:
            i_num, i_fact, i_city, i_country = i_line.split(':')
            if i_num[:3] == vin[:3]:
                result = f'{i_fact}, город: {i_city}, страна: {i_country[:-1]}'
    if not result:
        rez_path = os.path.join(os.getcwd(), 'func/data', 'WMI_RUS_lit.txt')
        with open(rez_path, 'r') as file:
            for i_line in file:
                i_num, i_fact, i_city, i_country = i_line.split(':')
                if i_num[:3] == vin[:3] and i_num[-4:-1] == vin[-6:-3]:
                    result = f'{i_fact}, город: {i_city}, страна: {i_country[:-1]}'
    if result:
        info['Завод в России'] = result
