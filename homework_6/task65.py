# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    speed = 0
    _color = ''
    __is_police = False

    def __init__(self, speed, color, is_police):
        self.speed = int(speed)
        self.color = color
        self.is_police = is_police

    def get_color(self):
        print(f'{self.color}')

    def get_is_police(self):
        print(f'{self.is_police}')

class TownCar(Car):
    def __init__(self, speed, color):
        super().__init__(int(speed), color, is_police=True)
        pass


if __name__ == '__main__':
    c = Car(100, "GREEN", False)
    c.get_color()
    c.get_is_police()

    c.color = "YELLOW"
    c.is_police = True
    c.get_is_police()
    c.get_color()

    c = TownCar(123, "RED")
    c.get_color()
    c.get_is_police()

    c.color = "GREY"
    c.is_police = False
    c.get_is_police()
    c.get_color()
