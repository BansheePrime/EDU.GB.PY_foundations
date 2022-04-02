#!/usr/bin/env python3
from itertools import zip_longest
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

new_list = zip(tutors, klasses)
print(f'{new_list}, zip() - generator-like object')
print(list(new_list))

print()

print('Убрали 2 последних элемента в списке klasses')
new_list = zip_longest(tutors, klasses[:-2])
print(list(new_list))

