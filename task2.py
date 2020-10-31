#Пользователь вводит время в секундах.
# Переведите время в часы, минуты
# и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

def secondsToTime(sec):
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    pattern = r'%02d:%02d:%02d'
    return pattern % (h, m, s)

if __name__ == '__main__':
    input = input("Введите время в секундах: ")
    sec = int(input)
    time = secondsToTime(sec)
    print(f'Time: {time}')