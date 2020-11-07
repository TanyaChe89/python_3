#Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def my_func(firstname, surname, birthdate, city, email, phone):
    print(f'имя={firstname}, фамилия={surname}, год рождения={birthdate}, г. проживания={city}, email={email}, телефон={phone}')


if __name__ == '__main__':

    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    birthdate = int(input("Введите год рождения: "))
    city = input("Введите город проживания: ")
    email = input("Введите email: ")
    phone = int(input("Введите телефон: "))

    my_func(firstname=name, surname=surname, birthdate=birthdate, city=city, email=email, phone=phone)
