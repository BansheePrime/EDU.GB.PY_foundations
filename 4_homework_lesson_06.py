#!/usr/bin/env python3
full_name = []
fio_list = []
hobby_name = []
sur_name = []
result_dict = {}

fio_file = open('users.csv')
for line in fio_file:
    full_name.append(line.strip().split(','))
fio_file.close()
# print(full_name)

hobby_file = open('hobby.csv')
for hobby_line in hobby_file:
    hobby_name = (hobby_line.strip().split(','))
hobby_file.close()
# print(hobby_name)

for fio in full_name:
    fio_list.append(str('').join(fio))
# print(fio_list)

for surname in full_name:
    sur_name.append(surname[0])
# print(sur_name)

result_dict = dict(zip(fio_list, hobby_name))
result_dict = {key: result_dict.get(key, None) for key in fio_list}
# print(result_dict)

with open('result.txt', 'w') as f:
    print(result_dict, file=f)

if len(full_name) < len(hobby_name):
    print(f'Хобби больше, чем людей. Exit code "1"')

