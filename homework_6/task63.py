# Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного
# имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

    def get_param(self, param):
        return self._income.get(param)


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
        pass

    def get_full_name(self):
        print(f'Fullname: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Total income: {int(self.get_param("wage"))+int(self.get_param("bonus"))}')


if __name__ == '__main__':
    name = input(f'Введите name ')
    surname = input(f'Введите surname ')
    position = input(f'Введите position ')
    wage = input(f'Введите wage ')
    bonus = input(f'Введите bonus ')

    p = Position(name, surname, position, wage, bonus)
    p.get_full_name()
    p.get_total_income()
