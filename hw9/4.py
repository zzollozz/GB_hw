""" 4. Реализуйте базовый класс Car:
    ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
    также методы: go, stop, turn(direction), которые должны сообщать, что машина
    поехала, остановилась, повернула (куда);
    ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
    ● добавьте в базовый класс метод show_speed, который должен показывать текущую
    скорость автомобиля;
    ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
    скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
    
    Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
    Вызовите методы и покажите результат. """


class Car:

    def __init__(self, name, color, speed, is_police=False):

        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f'{self.name} Начало движения')

    def stop(self):
        print(f'{self.name} Остановилась')

    def turn(self, direction):      # Поворот (direction) направление
        if direction.lower() == 'left':
            print(f'{self.name} повернула на лево')
        elif direction.lower() == 'right':
            print(f'{self.name} повернула на право')
        else:
            print(f'{self.name} задайте корректное направление!')

    def show_speed(self):
        print(f'Текущая скорость {self.name} составляет {self.speed} км/ч')


class TownCar(Car):     # Городской авто При значении  скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} превышении скорости!')
        else:
            print(f'Текущая скорость {self.name} составляет {self.speed} км/ч')


class SportCar(Car):    # Спортивный авто
    pass


class WorkCar(Car):     # Рабочий авто
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} превышении скорости!')
        else:
            print(f'Текущая скорость {self.name} составляет {self.speed} км/ч')


class PoliceCar(Car):   # Полицейский авто
    def __init__(self, name, color, speed, is_police=False):
        Car.__init__(self, name, color, speed, is_police=True)



towncar = TownCar('Лада', 'Синий', 80)
towncar.go()
towncar.show_speed()

sport_car = SportCar('Феррари', 'Красный', 240)
sport_car.go()
sport_car.turn('left')
sport_car.show_speed()
sport_car.turn('Right')
sport_car.stop()

police = PoliceCar('ДПС', 'Белый', 90)
police.go()
