# Для чисел в пределах от 20 до 240 найти числа,
# кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.


from random import randrange
from math import fmod

if __name__ == '__main__':
    print(randrange(20, 240, int(fmod(20, 240))))