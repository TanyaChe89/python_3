# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.

# Пользователь может продолжить ввод чисел, разделенных пробелом
# и снова нажать Enter. Сумма вновь введенных чисел будет добавляться
# к уже подсчитанной сумме. Но если вместо числа вводится
# специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,

# то вначале нужно добавить сумму этих чисел к полученной ранее сумме
# и после этого завершить программу.


if __name__ == '__main__':
    count = 0
    while True:
        input_string = input("Введите: ")

        symbols = input_string.split()
        print(f'Вы ввели: {symbols}')

        numbers = []
        for i in range(0, len(symbols)):
            if symbols[i].isdigit():
                num = int(symbols[i])
                numbers.append(num)
            else:
                print(f'Exit by symbol: {symbols[i]}')
                exit(0)

        count = count + sum(numbers)
        print(f'Сумма: {count}')