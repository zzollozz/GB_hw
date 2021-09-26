""" Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
 |--my_project
    |--settings
    |--mainapp
    |--adminapp
    |--authapp """
import os
import yaml
from yaml.loader import SafeLoader

# folders = ['my_project', 'settings', 'mainapp', 'adminapp', 'authapp']
#
# #
# if not os.path.isdir(folders[0]):
#     os.mkdir(folders[0])
#     os.chdir(folders[0])
#     for folder in folders[1:]:
#         hhh = os.path.join(os.getcwd(), folder)
#         os.mkdir(hhh)



# dir_path = os.path.join('my_project', 'settings', 'mainapp', 'adminapp', 'authapp')
# print(dir_path)
# if not os.path.exists(dir_path):  # Получилось каскадом (рекурсия папок)
#     os.makedirs(dir_path)

"""Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:"""

def directory_creation(path, names):
    for name in names:
        os.chdir(path)
        if isinstance(name, str):
            if name.find('.') != -1:
                file_creation(path, name)
            elif name not in os.listdir(path):
                os.mkdir(os.path.join(path, name))
            name_ = name
        else:
            directory_creation(os.path.join(path, name_), name)


def file_creation(path, name):
    if name not in os.listdir(path):
        with open(os.path.join(path, name), 'w', encoding='UTF-8') as file:
            file.write('')


with open('config.yaml', 'r', encoding='UTF-8') as f:
    folder_names = yaml.load(f, SafeLoader)
path = os.getcwd()



if __name__ == '__main__':
    directory_creation(path, folder_names)