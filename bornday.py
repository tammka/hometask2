year = input('Введите год рождения Пушкина: ')

if year == '1799':
    day = input('Введите день рождения Пушкина: ')
    if day in ['06.06', '6 июня']:
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год')