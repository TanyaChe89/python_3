# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение
# метода draw. Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    _title = 0

    def __init__(self, title):
        self._title = title

    def draw(self):
        print(f'“Запуск отрисовки.”')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
        pass

    def draw(self):
        print(f'Pen: Запуск отрисовки. ')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
        pass

    def draw(self):
        print(f'Pencil: Запуск отрисовки. ')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
        pass

    def draw(self):
        print(f'Handle: Запуск отрисовки. ')


if __name__ == '__main__':
    s = Stationery("Hammer")
    s.draw()

    s = Pen("Pen")
    s.draw()

    s = Pencil("Pencil")
    s.draw()

    s = Handle("Handle")
    s.draw()