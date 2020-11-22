# Реализуйте базовый класс Car. У данного класса должны быть
# следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда). Опишите несколько
# дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости
# свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f'Our speed: {self.speed}')

    def go(self):
        print(f'We are going')

    def stop(self):
        print(f'We are stoping')

    def turn(self, direction):
        print(f'We are turning: {direction}')

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(int(speed), color, name, is_police=False)
        pass

    def show_speed(self):
        print(f'Our speed: {self.speed}')
        if self.speed > 60:
            print(f'Cообщение о превышении скорости > 60')

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(int(speed), color, name, is_police=False)
        pass

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(int(speed), color, name, is_police=False)
        pass

    def show_speed(self):
        print(f'Our speed: {self.speed}')
        if self.speed > 40:
            print(f'Cообщение о превышении скорости > 40')

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(int(speed), color, name, is_police=True)
        pass


if __name__ == '__main__':

    tc = TownCar(65, "GREEN", "LADA")
    print(tc)
    tc.go()
    tc.stop()
    tc.turn("LEFT")
    tc.show_speed()

    tc = SportCar(100, "RED", "GREY")
    print(tc)
    tc.go()
    tc.stop()
    tc.turn("LEFT")
    tc.show_speed()

    tc = WorkCar(45, "YELLOW", "KIA")
    print(tc)
    tc.go()
    tc.stop()
    tc.turn("RIGHT")
    tc.show_speed()

    tc = PoliceCar(10, "BLACK", "SUBARU")
    print(tc)
    tc.go()
    tc.stop()
    tc.turn("RIGHT")
    tc.show_speed()