# Начните работу над проектом «Склад оргтехники». Создайте класс,
# описывающий склад. А также класс «Оргтехника», который будет
# базовым для классов-наследников. Эти классы — конкретные типы
# оргтехники (принтер, сканер, ксерокс). В базовом классе определить
# параметры, общие для приведенных типов. В классах-наследниках
# реализовать параметры, уникальные для каждого типа оргтехники.

from abc import ABC, abstractmethod


class Storage:
    size = "small"
    quipments = []

    def store(self, *equipments):
        self.quipments = list(equipments)
        print(f'Stored: {self.quipments}')

    def provide(self):
        for i in range(0, len(self.quipments)):
            print(self.quipments[i].do_something())


class OfficeEquipment:
    def __init__(self):
        print("Конструктор класса-родителя")

    @abstractmethod
    def do_something(self):
        pass

    def __str__(self):
        self.do_something()


class Printer(OfficeEquipment):

    def do_something(self):
        print(f"I'm printer")


class Scanner(OfficeEquipment):

    def do_something(self):
        print(f"I'm scanner")


class Xerox(OfficeEquipment):

    def do_something(self):
        print(f"I'm xerox")


if __name__ == '__main__':
    s1 = Scanner()
    s2 = Scanner()
    p1 = Printer()
    p2 = Printer()
    x1 = Xerox()
    x2 = Xerox()

    storage = Storage()
    storage.store(list[s1, s2, p1, p2, x1, x2])

