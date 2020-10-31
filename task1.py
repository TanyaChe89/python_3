# Поработайте с переменными,
# создайте несколько, выведите на экран,
#
# запросите у пользователя несколько чисел и
# строк и сохраните в переменные, выведите на экран

def print_variables():
    x = ['2', 4]
    z = True
    y = 123
    print(f'\n -> Simple variables: {x}; {y}; {z}')


if __name__ == '__main__':
    print_variables()
    userVariable = input("Введите ваше имя: ")
    print(f'Ваше имя - {userVariable}')
    userVariable = input("Введите ваш возраст: ")
    print(f'Ваш возраст - {userVariable}')
    userVariable = input("True or False: ")
    print({userVariable})