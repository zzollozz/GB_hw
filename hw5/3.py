# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>)
from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

""" Этот вариант я сам надумал после того как не получилось нагуглил второй вариант """
# result = []
# i = 0
# while i < len(tutors):
#     r = tutors[i] + klasses[i]
#     result.append(tuple([r]))
#     i += 1
# print(result)

""" Вариант 2 """

iterator = zip_longest(tutors, klasses[:len(tutors)])
print(list(iterator))



