# Создайте собственный класс-исключение, обрабатывающий ситуацию
# деления на нуль. Проверьте его работу на данных, вводимых
# пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


if __name__ == '__main__':

    inp_data = input("Введите 'XXX': ")

    try:
        if inp_data != "XXX":
            raise MyError(f"Вы ввели {inp_data}")
    except MyError as err:
        print(f'It is my error {err}')
    else:
        print(f"Все хорошо. Вы ввели: {inp_data}")

    try:
        print(100 / 0)
    except:
        print("Деление на ноль недопустимо")
