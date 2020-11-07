# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(a, b, c):
    my_list = [a, b, c]

    my_list.sort(reverse=True)

    return my_list[0] + my_list[1]


if __name__ == '__main__':
    a = 1
    b = 2
    c = 3

    result = my_func(a, b, c)

    print(result)
