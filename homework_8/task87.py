# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу
# проекта, создав экземпляры класса (комплексные числа) и выполнив
# сложение и умножение созданных экземпляров. Проверьте корректность
# полученного результата.


class ComplexNumber:
    param = 0

    def __init__(self, real, imag):
        self.param = complex(real, imag)

    def __str__(self):
        return f"ComplexNumber: ({self.param})"

    def __add__(self, other):
        real = self.param.real + other.param.real
        imag = self.param.imag + other.param.imag
        print(ComplexNumber(real, imag))

    def __mul__(self, other):
        real = self.param.real * other.param.real
        imag = self.param.imag * other.param.imag
        print(ComplexNumber(real, imag))


if __name__ == '__main__':
    c1 = ComplexNumber(4, 2)
    print(c1)

    c2 = ComplexNumber(3, 3)
    print(c2)

    c1 + c2
    c1 * c2