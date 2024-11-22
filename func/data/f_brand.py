n2 = {
    '1':  'Chevrolet',
    '2':  'Pontiac',
    '3':  'Oldsmobile',
    '4':  'Buick',
    '5':  'Pontiac',
    '6':  'Cadillac',
    '7':  'GM Canada',
    '8':  'Saturn',
    '9':  'Kia, Ford!', #???
    'A':  'Audi, Jaguar, Land Rover, Mitsubishi (США)',
    'B':  'BMW, Dodge',
    'C':  'Chrysler',
    'D':  'Dodge, Mercedes Benz',
    'F':  'Ford, Ferrari, Fiat, Subaru ',
    'G':  'General Motors ',
    'H':  'Acura, Honda, Lincoln ',
    'J':  'Jeep, Mercedes Benz (USA), !Nissan',
    'M':  'Hyundai, Mercury, Mitsubishi, Skoda ',
    'N':  'Infiniti, Nissan, Kia!',
    'O':  'Opel',
    'P':  'Plymouth',
    'S':  'Isuzu, Suzuki',
    'T':  'Lexus, Toyota',
    'U':  'BMW ',
    'V':  'Volvo, Volkswagen',
    'W':  'Kia'  #???
}


def rez_num_2(info, vin):
    if n2.get(vin[1]):
        info['Марка'] = n2.get(vin[1])
