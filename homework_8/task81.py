# Реализовать класс «Дата», функция-конструктор которого должна
# принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором
# @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором
# @staticmethod, должен проводить валидацию числа, месяца и
# года (например, месяц — от 1 до 12). Проверить работу
# полученной структуры на реальных данных.

class Data:
    __my_field = ""

    def __init__(self, string_date):
        self.__my_field = string_date

    @classmethod
    def parse_elements(cls, string_date):
        elements = string_date.split("-")
        print(f"Date: {int(elements[0])} Month: {int(elements[1])} Year: {int(elements[2])}")

    @staticmethod
    def validate_elements(string_date):
        elements = string_date.split("-")
        current_date = int(elements[0])

        if current_date < 30:
            print(f'Начало месяца, число = {current_date}')
        else:
            print(f'Конец месяца, число = {current_date}')

        months_dict = {1: 'январь',
                       2: 'февраль',
                       3: 'март',
                       4: 'апрель',
                       5: 'май',
                       6: 'июнь',
                       7: 'июль',
                       8: 'август',
                       9: 'сентябрь',
                       10: 'октябрь',
                       11: 'ноябрь',
                       12: 'декабрь'}

        current_month = elements[1]

        if months_dict.get(int(current_month), "XXX") == "XXX":
            print("Month not found")
        else:
            print(f'{months_dict.get(int(current_month), "XXX")}')

        current_year = elements[2]

        print(f'Current year: {current_year}')


if __name__ == '__main__':

    Data.parse_elements("01-11-2020")

    Data.validate_elements("01-11-2020")