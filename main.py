import datetime

FORMAT = "%H:%M:%S"
WEIGHT = 75
HEIGHT = 175
K_1 = 0.035
K_2 = 0.029

storage_dict = {}


def check_correct_data(data):
    """Проверка корректности полученного пакета."""
    if len(data) != 2:
        print('Пакет неверной длины')
        return False
    if None in data:
        print('Пакет содержит неверные данные')
        return False
    return True


def check_correct_time(time):
    """Проверка кореектности параметра времени."""
    if (time not in storage_dict and
       (not storage_dict or time > max(storage_dict))):
        return True
    return False


def get_step_day(steps):
    """Получить количество пройденных шагов за день"""
    day_steps = 0
    for key, value in storage_dict.items():
        day_steps += value['steps']
    return day_steps+steps


def get_distance(steps):
    """Получить дистанцию пройденного пути в км."""
    return (steps * 0.65)/1000


def get_spent_calories(dist, current_time):
    """Получение значения потреченных калорий."""
    time = current_time.hour + current_time.minute/60
    mean_speed = (dist / time)
    return (K_1*WEIGHT+(mean_speed**2//HEIGHT)*K_2*WEIGHT)*time*60


def accept_package(data):
    """Обработать пакет данных."""
    time, steps = data
    pack_time = datetime.datetime.strptime(time, FORMAT).time()
    if not(check_correct_data(data) and check_correct_time(pack_time)):
        return 'Некорректный пакет'

    day_steps = get_step_day(steps)
    dist = get_distance(day_steps)
    spent_calories = get_spent_calories(dist, pack_time)

    storage_dict[pack_time] = {'steps': steps}

    print(f'''
        Время: {pack_time}.
        За сегодня вы прошли {day_steps} шагов.
        Дистанция составила {dist:.2f} км.
        Вы сожгли {spent_calories:.2f} ккал.
        ''')
    return storage_dict


# Тесты
package = ('2:00:01', 15000)
package1 = ('11:00:02', 302)
accept_package(package)
accept_package(package1)
