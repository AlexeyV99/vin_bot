region = {
    'ABC': 'Африка',
    'DEFGHIJKLMNOPQR': 'Азия',
    'STUVWXYZ': 'Европа',
    '12345': 'Северная Америка',
    '67': 'Австралия, Новая Зеландия',
    '89': 'Южная Америка'
}

# Вычисление региона ТС
def rez_region(info, vin):
    for i_val, i_name in region.items():
        if vin[0] in i_val:
            info['Регион'] = i_name
    # return None


# print(rez_region('TMBLK7NE6K0123972'))
