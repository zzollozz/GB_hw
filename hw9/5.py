""" 5. Реализовать класс Stationery (канцелярская принадлежность):
    ● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
    сообщение «Запуск отрисовки»;
    ● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
    ● в каждом классе реализовать переопределение метода draw. Для каждого класса
    метод должен выводить уникальное сообщение;
    ● создать экземпляры классов и проверить, что выведет описанный метод для каждого
    экземпляра. """


class Stationery: # канцелярская принадлежность
    def __init__(self, title):
        self.title = title

    def draw(self, addition=None):
        print(f'Запуск отрисовки {addition}')


class Pen(Stationery):
    def draw(self, addition=None):
        Stationery.draw(self, addition=f'пишет {self.title}')


class Pencil(Stationery):
    def draw(self, addition=None):
        Stationery.draw(self, addition=f'пишет {self.title}')


class Handle(Stationery):
    def draw(self, addition=None):
        Stationery.draw(self, addition=f'пишет {self.title}')

pen = Pen('Ручка')
pencil = Pencil('Карандаш')
marker = Handle('Маркер')

pen.draw()
pencil.draw()
marker.draw()
