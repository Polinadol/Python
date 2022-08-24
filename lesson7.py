#1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
# класса (метод __init__()), который должен принимать данные (список списков)
# для формирования матрицы.
#Подсказка: матрица — система некоторых математических величин,
# расположенных в виде прямоугольной схемы.
#Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

#31    32         3    5    32        3    5    8    3
#37    43         2    4    6         8    3    7    1
#51    86        -1   64   -8
#Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#Далее реализовать перегрузку метода __add__() для реализации операции
# сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
#Подсказка: сложение элементов матриц выполнять поэлементно
# — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.

# class Matrix:
#     def __init__(self,list):
#         self.list=list
#
#     def __str__(self):
#         for row in list:
#             for i in row:
#                 print(f"{i:4}",end="")
#             print()
#         return ''
#     def __str__(self):
#          return '\n'.join(map(str, self.list))
#
#     def __add__(self, other):
#         for i in range(len(self.list)):
#             for i_2 in range(len(other.list[i])):
#                 self.list[i][i_2] = self.list[i][i_2] + other.list[i][i_2]
#         return Matrix.__str__(self)
# m=Matrix([[1,2,9],[0,-2,4],[3,2,4],[4,4,9]])
# m1=Matrix([[0,-3,4],[5,-7,2],[2,4,7],[2,-1,0]])
# print(m.__add__(m1))

# №2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные
# на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

# class Clothes:
#     def __init__(self,type):
#         self.type=type
#
#     @property
#     def consumption(self):
#         return f'ИТОГО ткани: {self.type / 6.5 + 0.5 + 2 * self.type + 0.3 :.2f}'
#
# #    abstractmethod
# #    def abstract(self):
# #        return '???'
# class Coat(Clothes):
#     def consumption(self):
#         return f'Для пошива пальто нужно: {self.type / 6.5 + 0.5 :.2f} ткани'
#
#     def abstract(self):
#         return 'Smth vary abstract second'
#
#
# class Costume(Clothes):
#     def consumption(self):
#         return f'Для пошива костюма нужно: {2 * self.type + 0.3 :.2f} ткани'
#
#     def abstract(self):
#         pass
#
#
# coat = Coat(800)
# costume = Costume(100)
# print(coat.consumption)
# print(costume.consumption())
# print(coat.abstract())

# class Cell:
#     def __init__(self, quantity):
#         self.quantity = int(quantity)
#
#     def __add__(self, other):
#         return f'Size: {self.quantity + other.quantity}'
#
#     def __sub__(self, other):
#         sub = self.quantity - other.quantity
#         return f'Size: {sub} ' if sub > 0 else ' no'
#
#     def __truediv__(self, other):
#         return self.quantity // other.quantity
#
#     def __mul__(self, other):
#         return self.quantity * other.quantity
#
#     def make_order(self, row):
#         result = ''
#         for i in range(int(self.quantity / row)):
#             result += '*' * row + '\n'
#         result += '*' * (self.quantity % row) + '\n'
#         return result
#
#
# cell = Cell(68)
# cell_2 = Cell(2)
# print(cell + cell_2)
# print(cell - cell_2)
# print(cell / cell_2)
# print(cell * cell_2)
# print(cell.make_order(7))