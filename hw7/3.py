""" Написать скрипт, который собирает все шаблоны в одну папку templates"""
import os
import shutil

project_folder = 'my_project'
templates = 'my_project/templates'

if not os.path.isdir(templates):
    os.mkdir(templates)
    shutil.copytree(project_folder, templates, copy_function=shutil.copy2, dirs_exist_ok=True)
else:
    print(f'папка с названием уже существует')
    print(os.listdir(os.path.join(os.getcwd(), 'my_project')))

