""" 3. Реализовать базовый класс Worker (работник):
    ● определить атрибуты: name, surname, position (должность), income (доход);
    ● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
    элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
    ● создать класс Position (должность) на базе класса Worker;
    ● в классе Position реализовать методы получения полного имени сотрудника
    (get_full_name) и дохода с учётом премии (get_total_income);
    ● проверить работу примера на реальных данных: создать экземпляры класса Position,
    передать данные, проверить значения атрибутов, вызвать методы экземпляров. """

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname  # Фамилия
        self.position = position    # должность
        self._income = {"wage": wage, "bonus": bonus}  # доход


class Position(Worker):

        def get_full_name(self):
            full_name = f'{self.name} {self.surname}'
            return full_name

        def get_total_income(self):
            income = self._income['wage'] + self._income['bonus']
            return income


worker = Position('Сергей', 'Петров', 'Кладовщик', 20, 5)

print(worker.get_full_name())
print(worker.get_total_income())
