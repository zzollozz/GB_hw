# """Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках), размер которых не превышает
#  этой границы, но больше предыдущей (начинаем с 0),"""
import os
from itertools import zip_longest
#
# folder_name = 'some_data'
# path = os.path.abspath('some_data')
# print(path)
# file_dir = os.listdir('some_data') # Список фалой в каталоге
#
# small_files = [] # Список размеров
# folder_statistics = {}
# i = 0
# n = 0
# for item in os.listdir(folder_name): # определение размера файла в папке
#     file_size = os.stat(os.path.join(folder_name, item)).st_size
#     small_files.append(file_size)
# for item in small_files:
#     if item <= 100:
#         i += 1
#     elif item <= 100 or item >= 1000:
#         n += 1
# print(i)
# print(n)
# dict_file = zip_longest(file_dir, small_files) # Словарь фалы и размер
# # print(small_files)
# # print(file_dir)
# print(dict(dict_file))
#
dict_rezult = {}    # Пустой словарь
path = os.path.join(os.getcwd(), 'some_data') # путь до папки с файлами
for root, dirs, files in os.walk(path): # разбор на путь дерикторию и файлы
    for file in files: # Перебор по фалов из спискоа
        file_size = os.stat(os.path.join(root, file)).st_size # определение размера выбранного файла
        n = 1 # определение позиции
        if file_size < n:
            if not dict_rezult.get(n):
                dict_rezult.setdefault(n, [1])
            else:
                dict_rezult[n][0] = dict_rezult[n][0] + 1
        else:
            while file_size > n:
                n = n * 10
                if file_size < n:
                    if not dict_rezult.get(n):
                        dict_rezult.setdefault(n, [1])
                    else:
                        dict_rezult[n][0] = dict_rezult[n][0] + 1
    # Сортировка полученого словаря
    list_keys = list(dict_rezult.keys())
    list_keys.sort()
    for el in list_keys:
        print(f'{el} : {dict_rezult[el]}')

