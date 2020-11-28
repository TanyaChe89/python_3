# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод init()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: см. в методичке.
#
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    _list_of_lists = []

    def __init__(self, list):
        self._list_of_lists = list

    def __str__(self):
        return f"Объект Matrix с параметрами ({self._list_of_lists})"

    def get_list(self):
        return self._list_of_lists

    def get_len_list(self):
        return len(self._list_of_lists)

    def __add__(self, other):
        list_of_lists = []
        for i in range(0, 2):
            internal_list_other = other.get_list()[i]
            internal_list_self = self.get_list()[i]
            internal_list = []
            for j in range(0, 2):
                internal_list.append(int(internal_list_self[j]) + int(internal_list_other[j]))
            list_of_lists.append(internal_list)

        return Matrix(list_of_lists)

if __name__ == '__main__':
    m1 = Matrix([list([1, 2]), list([3, 4])])
    print(m1)

    m2 = Matrix([list([5, 6]), list([7, 8])])
    print(m2)

    print(m1 + m2)

