# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

def convertAndCount(input):
    num1 = int(input) # 3
    num2 = int(input+input) # 33
    num3 = int(input+input+input) # 333
    return num1 + num2 + num3


if __name__ == '__main__':
    input = input("Введите n: ")
    result = convertAndCount(input)
    print(f'\n Result: {result}')