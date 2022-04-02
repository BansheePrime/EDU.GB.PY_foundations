#!/usr/bin/env python3
fio_file = open('users.csv')
for line in fio_file:
    full_name = (line.split(','))
    print(full_name)
fio_file.close()

hobby_file = open('hobby.csv')
for h_line in hobby_file:
    hobby_name = (h_line.strip().split(','))
    print(hobby_name)
hobby_file.close()

# useful_data = {}
# useful_data = dict.fromkeys(full_name, hobby_name)
# print(useful_data)