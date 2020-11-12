# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

import random


if __name__ == '__main__':
    number_list = []
    for i in range(0, 14):
        number_list.append(random.randint(0, 10))

    print(f'Исходный массив {number_list}')

    previous = 0
    current = 0
    new_list = []
    for i in range(1, len(number_list)):
        current = number_list[i]
        previous = number_list[i-1]
        if current <= previous:
            current = 0
            previous = 0
        else:
            new_list.append(current)

    print(f'Результат {new_list}')
