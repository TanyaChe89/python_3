# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

def defineMaxNumber(input):
    max = 0
    step = 0

    while step < len(input):
        symbol = input[step]
        num = int(symbol)
        if (max < num): max = num
        step = step + 1

    return max


if __name__ == '__main__':

    input = input("Введите положительное число: ")
    maxNumber = defineMaxNumber(input)
    print(f'\n Max: {maxNumber}')
