#1. Создать класс TrafficLight (светофор).
#определить у него один атрибут color (цвет) и метод running (запуск);
#атрибут реализовать как приватный;
#в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
#продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
#переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
#проверить работу примера, создав экземпляр и вызвав описанный метод.

#from time import sleep

#class TrafficLight:
#    _color=['Red','Yellow','Green']

#    def running(self):
#       i =0
#       while i !=3:
#           print(TrafficLight._color[i])
#           if i==0:
#               sleep(7)
#           elif i==1:
#               sleep(2)
#           elif i==2:
#               sleep(4)
#           i +=1

#t= TrafficLight()
#t.running()

#2. Реализовать класс Road (дорога).
#определить атрибуты: length (длина), width (ширина);
#значения атрибутов должны передаваться при создании экземпляра класса;
#атрибуты сделать защищёнными;
#определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
#использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
#проверить работу метода.

#class Road:
#    def __init__(self,length,width):
#        self.length=length
#        self.width=width
#        self.mass= 100
#        self.height=5

#    def road_mass(self):

#         road_mass=self.length*self.width*self.mass*self.height/1000
#         print(f'Итого масса асфальта: {road_mass} тонн')
#r=Road(20,5)
#r.road_mass()

#3. Реализовать базовый класс Worker (работник).
#определить атрибуты: name, surname, position (должность), income (доход);
#последний атрибут должен быть защищённым и ссылаться на словарь,
#содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
#создать класс Position (должность) на базе класса Worker;
#в классе Position реализовать методы получения полного имени сотрудника
#(get_full_name) и дохода с учётом премии (get_total_income);
#проверить работу примера на реальных данных: создать экземпляры класса
#Position, передать данные, проверить значения атрибутов,
#вызвать методы экземпляров.

#class Worker:
#    def __init__(self, name,surname, position, wage,bonus):
#        self.name=name
#        self.surname=surname
#        self.position=position
#        self._income ={"wage":int(wage),"bonus":int(bonus)}

#class Position(Worker):
#    def __init__(self, name,surname, position, wage,bonus):
#        super().__init__(name,surname, position, wage,bonus)
#    def get_full_name(self):
#        return self.name +' ' +self.surname
#    def get_total_income(self):
#        return self._income["wage"]+self._income["bonus"]

#p=Position('Petr','Ivanov','superviser',150000,100000)
#print(p.get_full_name())
#print(p.get_total_income())

#4. Реализуйте базовый класс Car.
#у класса должны быть следующие атрибуты: speed, color, name, is_police
#(булево). А также методы: go, stop, turn(direction), которые должны
#сообщать, что машина поехала, остановилась, повернула (куда);
#опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
#добавьте в базовый класс метод show_speed, который должен показывать
#текущую скорость автомобиля;
#для классов TownCar и WorkCar переопределите метод show_speed.
#При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
#выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов.
#Выполните доступ к атрибутам, выведите результат.
#Вызовите методы и покажите результат.

#class Car:
#    def __init__(self, speed,color,name,is_police=False):
#        self.speed=speed
#        self.color=color
#        self.name=name
#        self.is_police=is_police

#    def go(self):
#        return f' Машина {self.name} поехала'
#    def stop(self):
#        return f' Машина {self.name} остановаилась'
#    def turn(self):
#        return f' Машина {self.name} повернула'
#    def show_speed(self):
#        return f' Машина {self.name} едет со скоростью {self.speed}'
#c=Car(100,'Red','TOYOTA',True)
#print(c.go())

#class TownCar(Car):
#    def show_speed(self):
#        def __init__(self,speed,color,name,is_police=False):
#            super().__init__(speed,color,name,is_police=False)
#            if self.speed>60:
#                return f'Скорость превышена'
#            else:
#                return f'Скорость в норме'

#class SportCar(Car):
#    pass

#class WorkCar(Car):
#    def show_speed(self):
#        def __init__(self,speed,color,name,is_police=False):
#            super().__init__(speed,color,name,is_police=False)
#            if self.speed>40:
#                return f'Скорость превышена'
#            else:
#                return f'Скорость в норме'


#class PoliceCar(Car):
#    pass

#town=TownCar(100,'Red','TOYOTA',False)
#print(town.go(),town.show_speed(),town.turn()+ ' налево',town.stop())

#sport=SportCar(90,'Blue','Mazda',False)
#print(sport.go(),sport.show_speed(),sport.turn()+ ' направо',sport.stop())

#work=WorkCar(30,'Black','BMW',False)
#print(work.go(),work.show_speed(),work.turn()+ ' направо',work.stop())

#police=PoliceCar(50,'White','OPEL',True)
#print(police.go(),police.show_speed(),police.turn()+ ' направо',police.stop())

#5. Реализовать класс Stationery (канцелярская принадлежность).
#определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
#создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер);в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
#создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

#class Stationery():
#    def __init__(self,title):
#        self.title=title
#    def draw(self):
#        return f'Запуск отрисовки {self.title}'
#s=Stationery('общий')
#print(s.draw())

#class Handle(Stationery):
#    def draw(self):
#        return f'Запуск отрисовки {self.title}'
#h=Handle('маркером')
#print(h.draw())

#class Pencil(Stationery):
#    def draw(self):
#        return f'Запуск отрисовки {self.title}'
#p=Pencil('карандашом')
#print(p.draw())

#class Pen(Stationery):
#    def draw(self):
#        return f'Запуск отрисовки {self.title}'
#pen=Handle('ручкой')
#print(pen.draw())