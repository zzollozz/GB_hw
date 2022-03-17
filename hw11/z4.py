import json
""" 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
    А также класс «Оргтехника», который будет базовым для классов-наследников. 
    Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
    В базовом классе определите параметры, общие для приведённых типов.
    В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
    
    5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад
    и передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
    а также других данных, можно использовать любую подходящую структуру (например, словарь)."""



class WarehouseOfOfficeEquipment:   # Склад оргтехники
    def __init__(self, name, model, quantity, subdivision_1, subdivision_2=None):
        self.name = name
        self.model = model
        self.quantity = quantity
        self.subdivision = subdivision_1
        self.subdivision_2 = subdivision_2


    @staticmethod
    def coming(self):   # Приход
        try:
            if self.name.lower() == 'принтер' or 'принтеры':
                with open('printers.json') as f:
                    printers = json.load(f)

                next_namber = {}
                next_namber['модель'] = self.model.upper()
                next_namber['количество'] = self.quantity
                next_namber['подразделение'] = self.subdivision.capitalize()

                for k, v in list(printers.items()):
                    if self.model.upper() in list(v.values()) and self.subdivision.capitalize() in list(v.values()):
                        poz = k
                        flag = True
                        break
                    elif self.model.upper() not in list(v.values()) and self.subdivision.capitalize() in list(v.values()):
                        flag = False

                if flag == True:
                    printers[poz]['количество'] += self.quantity
                    print(f'==== Выполнено ====\n{printers[poz]}')
                elif flag == False:
                    printers[int(max(printers.keys())) + 1] = next_namber

                with open('printers.json', 'w', encoding='utf-8') as f:
                    json.dump(printers, f, indent=2, ensure_ascii=False)


            if self.name.lower() == 'сканер' or 'сканеры':
                with open('scanner.json') as f:
                    scanner = json.load(f)

                next_namber = {}
                next_namber['модель'] = self.model.upper()
                next_namber['количество'] = self.quantity
                next_namber['подразделение'] = self.subdivision.capitalize()

                for k, v in list(scanner.items()):
                    if self.model.upper() in list(v.values()) and self.subdivision.capitalize() in list(v.values()):
                        poz = k
                        flag = True
                        break
                    elif self.model.upper() not in list(v.values()) and self.subdivision.capitalize() in list(
                            v.values()):
                        flag = False

                if flag == True:
                    scanner[poz]['количество'] += self.quantity
                    print(f'==== Выполнено ====\n{scanner[poz]}')
                elif flag == False:
                    scanner[int(max(scanner.keys())) + 1] = next_namber

                with open('scanner.json', 'w', encoding='utf-8') as f:
                    json.dump(scanner, f, indent=2, ensure_ascii=False)

            if self.name.lower() == 'ксерокс':
                with open('xerox.json') as f:
                    xerox = json.load(f)

                next_namber = {}
                next_namber['модель'] = self.model.upper()
                next_namber['количество'] = self.quantity
                next_namber['подразделение'] = self.subdivision.capitalize()

                for k, v in list(xerox.items()):
                    if self.model.upper() in list(v.values()) and self.subdivision.capitalize() in list(v.values()):
                        poz = k
                        flag = True
                        break
                    elif self.model.upper() not in list(v.values()) and self.subdivision.capitalize() in list(
                            v.values()):
                        flag = False

                if flag == True:
                    xerox[poz]['количество'] += self.quantity
                    print(f'==== Выполнено ====\n{xerox[poz]}')
                elif flag == False:
                    xerox[int(max(xerox.keys())) + 1] = next_namber

                with open('xerox.json', 'w', encoding='utf-8') as f:
                    json.dump(xerox, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f' Ошибка ввода данных: {e}')


    @staticmethod
    def consumption(self): # Расход
        try:
            if self.name.lower() == 'принтер' or 'принтеры':
                with open('printers.json') as f:
                    printers = json.load(f)

            for k, v in printers.items():
                if self.model.upper() in list(v.values()) and self.subdivision.capitalize() in list(v.values()):
                    poz = k
                    flag = True
                    break
                elif self.model.upper() not in list(v.values()) and self.subdivision.capitalize() in list(v.values()):
                    flag = False

            if flag == True:
                if printers[poz]['количество'] > self.quantity:
                    printers[poz]['количество'] -= self.quantity

                    next_namber = {}
                    next_namber['модель'] = self.model.upper()
                    next_namber['количество'] = self.quantity
                    next_namber['подразделение'] = self.subdivision_2.capitalize()

                    for k, v in list(printers.items()):
                        if self.model.upper() in list(v.values()) and self.subdivision_2.capitalize() in list(v.values()):
                            poz = k
                            flag_2 = True
                        elif self.model.upper() in list(v.values()) and self.subdivision_2.capitalize() not in list(v.values()):
                            flag_2 = False

                    if flag_2:
                        printers[poz]['количество'] += self.quantity
                        print(f'==== Выполнено ====\n{printers[poz]}')
                    elif flag_2 == False:
                        printers[int(max(printers.keys())) + 1] = next_namber

                    with open('printers.json', 'w', encoding='utf-8') as f:
                        json.dump(printers, f, indent=2, ensure_ascii=False)
                else:
                    print(f'указанная позиция {self.model.upper()} в подразделении {self.subdivision.capitalize()} меньше расхода!!! Операция не выполнима')

            elif flag == False:
                print(f'в подразделение - {self.subdivision.capitalize()} - такой модели: {self.model.upper()} -нет')

            if self.name.lower() == 'сканер' or 'сканеры':
                with open('scanner.json') as f:
                    scanner = json.load(f)

            for k, v in scanner.items():
                if self.model.upper() in list(v.values()) and self.subdivision.capitalize() in list(v.values()):
                    poz = k
                    flag = True
                    break
                elif self.model.upper() not in list(v.values()) and self.subdivision.capitalize() in list(v.values()):
                    flag = False

            if flag == True:
                if scanner[poz]['количество'] > self.quantity:
                    scanner[poz]['количество'] -= self.quantity

                    next_namber = {}
                    next_namber['модель'] = self.model.upper()
                    next_namber['количество'] = self.quantity
                    next_namber['подразделение'] = self.subdivision_2.capitalize()

                    for k, v in list(scanner.items()):
                        if self.model.upper() in list(v.values()) and self.subdivision_2.capitalize() in list(v.values()):
                            poz = k
                            flag_2 = True
                        elif self.model.upper() in list(v.values()) and self.subdivision_2.capitalize() not in list(v.values()):
                            flag_2 = False

                    if flag_2:
                        scanner[poz]['количество'] += self.quantity
                        print(f'==== Выполнено ====\n{scanner[poz]}')
                    elif flag_2 == False:
                        scanner[int(max(printers.keys())) + 1] = next_namber

                    with open('scanner.json', 'w', encoding='utf-8') as f:
                        json.dump(scanner, f, indent=2, ensure_ascii=False)
                else:
                    print(f'указанная позиция {self.model.upper()} в подразделении {self.subdivision.capitalize()} меньше расхода!!! Операция не выполнима')

            elif flag == False:
                print(f'в подразделение - {self.subdivision.capitalize()} - такой модели: {self.model.upper()} -нет')

            if self.name.lower() == 'ксерокс' or 'ксероксы':
                with open('xerox.json') as f:
                    xerox = json.load(f)

            for k, v in xerox.items():
                if self.model.upper() in list(v.values()) and self.subdivision.capitalize() in list(v.values()):
                    poz = k
                    flag = True
                    break
                elif self.model.upper() not in list(v.values()) and self.subdivision.capitalize() in list(v.values()):
                    flag = False

            if flag == True:
                if xerox[poz]['количество'] > self.quantity:
                    xerox[poz]['количество'] -= self.quantity

                    next_namber = {}
                    next_namber['модель'] = self.model.upper()
                    next_namber['количество'] = self.quantity
                    next_namber['подразделение'] = self.subdivision_2.capitalize()

                    for k, v in list(xerox.items()):
                        if self.model.upper() in list(v.values()) and self.subdivision_2.capitalize() in list(v.values()):
                            poz = k
                            flag_2 = True
                        elif self.model.upper() in list(v.values()) and self.subdivision_2.capitalize() not in list(v.values()):
                            flag_2 = False

                    if flag_2:
                        xerox[poz]['количество'] += self.quantity
                        print(f'==== Выполнено ====\n{xerox[poz]}')
                    elif flag_2 == False:
                        xerox[int(max(printers.keys())) + 1] = next_namber

                    with open('xerox.json', 'w', encoding='utf-8') as f:
                        json.dump(xerox, f, indent=2, ensure_ascii=False)
                else:
                    print(f'указанная позиция {self.model.upper()} в подразделении {self.subdivision.capitalize()} меньше расхода!!! Операция не выполнима')

            elif flag == False:
                print(f'в подразделение - {self.subdivision.capitalize()} - такой модели: {self.model.upper()} -нет')
        except Exception as e:
            print(f' Ошибка ввода данных: {e}')


class OfficeEquipment:
    def __init__(self, name):
        self._name = name

    def printing(self):
        print(f'{self._name} Печатаю ч/б')


class Printer(OfficeEquipment):
    def printing_color(self):
        print(f'{self._name} Печатаю в цвете')


class Scanner(OfficeEquipment):
    def scan(self):
        print(f'{self._name} Сканирую')


class Xerox(OfficeEquipment):
    def copi(self):
        print(f'{self._name} Копирую')

if __name__ == '__main':
    # printer = Printer('Принтер')
    # scaner = Scanner('Сканер')
    #
    # printer.printing_color()
    # scaner.printing()
    # scaner.scan()

    # Приход на склад

    WarehouseOfOfficeEquipment.coming(WarehouseOfOfficeEquipment('Принтер', 'Canon TS-100', 1, 'Склад'))

    # WarehouseOfOfficeEquipment.coming(WarehouseOfOfficeEquipment('принтер', 'Canon TS-100', 2))
    # WarehouseOfOfficeEquipment.coming(WarehouseOfOfficeEquipment('принтер', 'Epson SA-232', 1))
    # WarehouseOfOfficeEquipment.coming(WarehouseOfOfficeEquipment('сканер', 'Epson A-000', 1))
    # WarehouseOfOfficeEquipment.coming(WarehouseOfOfficeEquipment('ксерокс', 'Canon Wde-999', 2))
    # WarehouseOfOfficeEquipment.coming(WarehouseOfOfficeEquipment('сканер', 'CANON S-232', 1))
    # WarehouseOfOfficeEquipment.coming(WarehouseOfOfficeEquipment(12, 'CANON S-232', 1))


