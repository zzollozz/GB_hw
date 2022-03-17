a=0
""" 6. Продолжить работу над вторым заданием. 
    Реализуйте механизм валидации вводимых пользователем данных.
    Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП."""
import json
from hw11.z4 import WarehouseOfOfficeEquipment

def open_product(produkt):
    match produkt:
        case 'принтеры' | 'принтер':
            file = 'printers.json'
        case 'сканеры' | 'сканер':
            file = 'scanner.json'
        case 'ксероксы' | 'ксерокс':
            file = 'xerox.json'
    with open(file) as f:
         print(json.load(f))

def work():
    oper = input('Какую операцию выполнить (Приход, Расход): ').lower()
    match oper:
        case 'приход':
            name = input('Укажите категорию техники: ')
            model = input('Укажите модель: ')
            quantity = int(input('Укажите количество: '))
            subdivision = input('Укажите подразделение: ')
            WarehouseOfOfficeEquipment.coming(WarehouseOfOfficeEquipment(name, model, quantity, subdivision))
        case 'расход':
            name = input('Укажите категорию техники: ')
            model = input('Укажите модель: ')
            quantity = int(input('Укажите количество: '))
            subdivision = input('Укажите с какого подразделения: ')
            subdivision_2 = input('Укажите в какое подразделение: ')
            WarehouseOfOfficeEquipment.consumption(
                WarehouseOfOfficeEquipment(name, model, quantity, subdivision, subdivision_2))
        case _:
            print()

while True:
    try:
        start = input('УЧЕТ ОРГТЕХНИКИ ПО ПОДРАЗДЕЛЕНИЯМ\nЖелаете посмотреть наличие? (Да, Нет, Выход): ').lower()
        if start == 'да':
            produkt = input('Укажите продукт (Принтеры, Сканеры, Ксероксы): ').lower()
            open_product(produkt)
            work()
        elif start == 'нет':
            work()
        elif start == 'выход':
            print('*** END ***')
            break
    except Exception as e:
        print(f' Ошибка ввода данных: {e}')








# WarehouseOfOfficeEquipment.coming(WarehouseOfOfficeEquipment('Принтер', 'XXXx XX-100', 100, 'Склад'))
# WarehouseOfOfficeEquipment.coming(WarehouseOfOfficeEquipment('Принтер', 'samsung v-5', 4, 'Склад'))

# WarehouseOfOfficeEquipment.consumption(WarehouseOfOfficeEquipment('Принтер', 'Canon TS-100', 1, 'Склад', 'Офис'))
# WarehouseOfOfficeEquipment.consumption(WarehouseOfOfficeEquipment('Принтер', 'Canon TS-100', 1, 'Офис', 'Склад'))
# WarehouseOfOfficeEquipment.consumption(WarehouseOfOfficeEquipment('Принтер', 'Canon TS-700', 1, 'Офис', 'Склад'))
# WarehouseOfOfficeEquipment.consumption(WarehouseOfOfficeEquipment('Принтер', 'EXEN T-500', 1, 'Склад', 'Офис'))
