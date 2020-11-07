#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def my_func(first, second):
    return first/second


if __name__ == '__main__':
    first = int(input("Введите первое число: "))# 1
    second = int(input("Введите второе число: ")) #2

    if(second == 0): #3
        print("Делить на ноль нельзя")
    else:
        result = my_func(first, second)
        print(result)

