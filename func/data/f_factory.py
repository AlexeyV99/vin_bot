import os


def rez_wim(info, vin):
    rez_path = os.path.join(os.getcwd(), 'func/data', 'WMI_code.txt')
    with open(rez_path, 'r') as file:
        for i_line in file:
            i_num, i_reg = i_line.split(':')
            if i_num[:3] == vin[:3]:
                info['Производитель'] = i_reg[:-1]
