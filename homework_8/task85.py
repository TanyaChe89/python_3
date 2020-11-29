#  Продолжить работу над первым заданием. Разработать методы,
#  отвечающие за приём оргтехники на склад и передачу в
#  определенное подразделение компании. Для хранения данных о
#  наименовании и количестве единиц оргтехники, а также других данных,
#  можно использовать любую подходящую структуру, например словарь.

from abc import ABC, abstractmethod


class Storage:
    size = "small"
    subjects = []
    stored = {}

    def __init__(self, *subjects):
        self.subjects = subjects
        for eq in subjects:
            if eq.who_am_i() == "PRINTER":
                count = self.stored.get("PRINTER", 0)
                self.stored["PRINTER"] = count + 1
            elif eq.who_am_i() == "SCANNER":
                count = self.stored.get("SCANNER", 0)
                self.stored["SCANNER"] = count + 1
            elif eq.who_am_i() == "XEROX":
                count = self.stored.get("XEROX", 0)
                self.stored["XEROX"] = count + 1

    def provide(self):
        for i in range(0, len(self.subjects)):
            self.subjects[i].do_something()

    def get_count(self, name):
        print(self.stored.get(name, 0))

class OfficeEquipment:
    def __init__(self):
        print("Конструктор OfficeEquipment вызван")

    @abstractmethod
    def do_something(self):
        pass

    @abstractmethod
    def who_am_i(self):
        pass

    def __str__(self):
        self.do_something()


class Printer(OfficeEquipment):

    def do_something(self):
        print(f"I'm printer")

    def who_am_i(self):
        return "PRINTER"


class Scanner(OfficeEquipment):

    def do_something(self):
        print(f"I'm scanner")

    def who_am_i(self):
        return "SCANNER"


class Xerox(OfficeEquipment):

    def do_something(self):
        print(f"I'm xerox")

    def who_am_i(self):
        return "XEROX"


if __name__ == '__main__':
    s1 = Scanner()
    s2 = Scanner()
    p1 = Printer()
    p2 = Printer()
    x1 = Xerox()
    x2 = Xerox()

    storage = Storage(s1, s2, p1, p2, x1, x2)
    storage.provide()

    storage.get_count("PRINTER")