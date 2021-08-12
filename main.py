import datetime as dt

FORMAT = "%H:%M:%S"
WEIGHT = 75  # Вес
HEIGHT = 175  # Рост
K_1 = 0.035  # Коэффициент для подсчета калорий
K_2 = 0.029  # Коэффициент для подсчета калорий
STEP_M = 0.65  # Длина шага в метрах

storage_data = {}


def check_correct_data(data):
    """Проверка корректности полученного пакета."""
    if len(data) != 2 or None in data:
        return False
    return True


def check_correct_time(time):
    """Проверка кореектности параметра времени."""
    if storage_data and time <= max(storage_data):
        return False
    return True


def get_step_day(steps):
    """Получить количество пройденных шагов за день."""
    day_steps = 0
    for key, value in storage_data.items():
        day_steps += value
    return day_steps+steps


def get_distance(steps):
    """Получить дистанцию пройденного пути в км."""
    return (steps * STEP_M)/1000


def get_spent_calories(dist, current_time):
    """Получить значения потраченных калорий."""
    time = current_time.hour + current_time.minute/60
    mean_speed = (dist / time)
    return (K_1*WEIGHT+(mean_speed**2//HEIGHT)*K_2*WEIGHT)*time*60


def get_achievement(dist):
    """Получить поздравления за пройденную дистанцию."""
    if dist < 2:
        return 'Лежать тоже полезно. Главное — участие, а не победа!'
    if dist < 3.9:
        return 'Маловато, но завтра наверстаем!'
    if dist < 6.5:
        return 'Неплохо! День был продуктивным.'
    return 'Отличный результат! Цель достигнута.'


def show_message(time, steps, dist, calories, achiev):
    """Вывести на экран результаты вычислений"""
    print(f'''
Время: {time}.
За сегодня вы прошли {steps} шагов.
Дистанция составила {dist:.2f} км.
Вы сожгли {calories:.2f} ккал.
{achiev}
        ''')


def accept_package(data):
    """Обработать пакет данных."""
    time, steps = data
    pack_time = dt.datetime.strptime(time, FORMAT).time()
    if not(check_correct_data(data) and check_correct_time(pack_time)):
        return 'Некорректный пакет'

    day_steps = get_step_day(steps)
    dist = get_distance(day_steps)
    spent_calories = get_spent_calories(dist, pack_time)
    achievement = get_achievement(dist)
    show_message(pack_time, day_steps, dist,
                 spent_calories, achievement)

    storage_data[pack_time] = steps

    return storage_data


# Тесты
package = ('2:00:01', 15000)
package1 = ('2:00:02', 302)
accept_package(package)
print(storage_data)
accept_package(package1)
print(storage_data)
