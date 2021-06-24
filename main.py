import datetime

FORMAT = "%H:%M:%S"

storage_dict = {}


def check_correct_data(data):
    """Проверка корректности полученного пакета."""
    if len(data) != 3:
        print('Пакет неверной длины')
        return False
    elif None in data:
        print('Пакет содержит неверные данные')
        return False
    else:
        return True


def get_status_pulse(pulse):
    """Получить статус тренировки по показанию пульса."""
    if pulse <= 110:
        return '"Вы отдыхатете"'
    elif pulse <= 130:
        return '"Тренеровка на жиросжигание"'
    elif pulse <= 160:
        return '"Высокоинтенсивная тренеровка"'
    elif pulse <= 200:
        return '"Высокая нагрузка"'
    else:
        return '"Возможен вред здоровью"'


def get_param_distance():
    """Получить параметры пройденного пути."""
    day_steps = 0
    for key, value in storage_dict.items():
        day_steps += value['steps']
    dist_km = (day_steps * 0.65) / 1000
    spent_calories = dist_km * 200
    return day_steps, dist_km, spent_calories


def accept_package(data):
    """Получение пакета данных."""
    if check_correct_data(data):
        print('Пакет корректен')
        time, steps, pulse = data
        pack_time = datetime.datetime.strptime(time, FORMAT)
        if pack_time.time() not in storage_dict \
           and (not storage_dict or pack_time.time() > max(storage_dict)):
            storage_dict[pack_time.time()] = {'steps': steps, 'pulse': pulse}
            day_steps, dist_km, spent_calories = get_param_distance()
            print(f'''
                Время: {pack_time.time()}.
                За сегодня вы прошли {day_steps} шагов.
                Дистанция составила {dist_km} км.
                Вы сожгли {spent_calories}.
                Текущий статус тренеровки {get_status_pulse(pulse)}.
                ''')


package = ('11:00:01', 302, 100)
package1 = ('11:00:02', 302, 100)
accept_package(package)
accept_package(package1)
