#1. Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

# class Data:
#     def __init__(self, dd_mm_yy):
# #        self.dd=dd
# #        self.mm=mm
# #        self.yy=yy
#         self.dd_mm_yy=str(dd_mm_yy)
#
#     @classmethod
#     def extract(cls, dd_mm_yy):
#         date = []
#
#         for i in dd_mm_yy.split():
#             if i != '-': date.append(i)
#
#         return int(date[0]), int(date[1]), int(date[2])
#
#
#     @staticmethod
#     def valid(dd, mm, yy):
#         if 1 <= dd <= 31:
#             if 1 <= mm <= 12:
#                 if 2022 >= yy >= 0:
#                     return f'All right'
#                 else:
#                     return f'Неправильный год'
#             else:
#                 return f'Неправильный месяц'
#         else:
#             return f'Неправильный день'
#
#
#     def __str__(self):
#         return f'Сегодня {Data.extract(self.dd_mm_yy)}'
#
#
#
# today = Data('8 - 7 - 2022')
# print(today)
# print(Data.valid(12, 12, 2007))
# print(today.valid(33, 28, 2011))
# print(Data.extract('8 - 9 - 1987'))
# print(today.extract('18 - 12 - 2005'))
# print(Data.valid(8, 9, 1987))

#2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.

# class DivideNull:
#     def __init__(self,chislitel,znamenatel):
#         self.chislitel=chislitel
#         self.znamenatel=znamenatel
#
#     @staticmethod
#     def division(chislitel,znamenatel):
#         try:
#             return chislitel/znamenatel
#         except:
#             return (f'НЕЛЬЗЯ ДЕЛИТЬ НА 0!')
#
# div=DivideNull(100,10)
# print(div.division(100,20))
# print(div.division(100,0))

#3. Создайте собственный класс-исключение, который должен проверять содержимое списка на
# наличие только чисел. Проверить работу исключения на реальном примере. Запрашивать у
# пользователя данные и заполнять список необходимо только числами. Класс-исключение должен
# контролировать типы данных элементов списка.
#Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь
# сам не остановит работу скрипта, введя, например, команду «stop». При этом скрипт завершается,
# сформированный список с числами выводится на экран.
#Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
# Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
# Вносить его в список, только если введено число. Класс-исключение должен не позволить
# пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

# class Test(Exception):
#     def __init__(self,numbers):
#         self.numbers=numbers
#
#     def __str__(self):
#        return self.numbers
#
# if __name__ == '__main__':
#     my_list=[]
#     while True:
#         vvod= input('Введите числа через пробел или введите STOP:   ')
#         if vvod == 'STOP':
#             break
#         try:
#             if not vvod.isdigit():
#                 raise Test(f'Введены числа')
#             my_list.append(int(vvod))
#         except Test as t:
#             print(t)
#
#     print(my_list)

#7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число». Реализуйте перегрузку методов
# сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

# class ComplexNum:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         self.c='a+b*i'
#     def __add__(self, other):
#         return f'c={self.a+other.a}+{self.b+other.b}*i'
#         print(f'Сумма чисел равна:   ')
#     def __mul__(self, other):
#         return f'c={self.a * other.a}+{self.b * other.b}*i'
#         print(f'Сумма чисел равна:   ')
#
# c1=ComplexNum(2,4)
# c2=ComplexNum(6,5)
# print(c1)
# print(c1+c2)
# print(c1*c2)

#4. Начните работу над проектом «Склад оргтехники». Создайте класс,
# описывающий склад. А также класс «Оргтехника», который будет
# базовым для классов-наследников. Эти классы — конкретные типы
# оргтехники (принтер, сканер, ксерокс). В базовом классе определите
# параметры, общие для приведённых типов. В классах-наследниках
# реализуйте параметры, уникальные для каждого типа оргтехники.
#
# class Technica:
#     def __init__(self, name,amount, price,firm):
#         self.name=name
#         self.amount=amount
#         self.price=price
#         self.firm=firm
#         self.magazin=[]
#         self.my_tech={'Название':self.name, 'Количество':self.amount, 'Цена':self.price, 'Производитель':self.firm}
#
#     def __str__(self):
#         return f'Название   {self.name}, Количество   {self.amount}, Цена   {self.price}, Производитель   {self.firm}'
#
#
#
#
#
#     #@classmethod
#     #@staticmethod
#     def insert(self):
#         #while True:
#         try:
#             name = input(f'Введите наименование ')
#             price = int(input(f'Введите цену за ед '))
#             amount = int(input(f'Введите количество '))
#             object = {'Модель устройства': name, 'Цена за ед': price, 'Количество': amount}
#             self.my_tech.update(object)
#             self.magazin.append(self.my_tech)
#             print(f'Текущий список -\n {self.my_tech}')
#         except:
#             return f'Ошибка ввода данных'
#
# class Printer(Technica):
#     def __init__(self,name, amount, price, firm, weight):
#         self.name = name
#         self.amount = amount
#         self.price = price
#         self.firm = firm
#         self.weight = weight
#         super().__init__(name, amount, price, firm,weight)
#     def to_print(self):
#         return f'Новый параметр {self.weight} кг'
#
# class Scanner(Technica):
#     def __init__(self,name,amount,price,firm, display):
#         self.name = name
#         self.amount = amount
#         self.price = price
#         self.firm = firm
#         self.display = display
#         super().__init__(name,amount,price,firm)
#     def to_scan(self):
#         return f'Количество дисплеев {self.display} шт'
#
# my_tech1=Technica('Canon', 2,400,'Japan')
# my_tech2=Technica('Xerox', 8,600,'China')
# print(my_tech1)
# print(my_tech2)
# new=Printer('HP',2,500,'Koreya')
# print(new)
#
#
#
#
# my_tech3 = Printer('hp', 2000, 5, 10)
# my_tech4 = Scanner('Canon', 1200, 5, 10)
# print(my_tech2.insert())
# print(my_tech4.insert())
# print(name.to_print())
# print(price.to_scan())