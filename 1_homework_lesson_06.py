#!/usr/bin/env python3
file = open('nginx_logs.txt')
result_data = []
remote_addr = []

for line in file:
    clean_data = line.replace('"', '').split()
    remote_addr.append(clean_data[0])
    useful_line = (clean_data[0], clean_data[5], clean_data[6])
    result_data.append(useful_line)
# print(tuple(result_data))
# print(remote_addr)

def most_frequent(some_list):
    return max(set(some_list), key = some_list.count)

print(f'Руки вверх, {most_frequent(remote_addr)}, ты похож на спамера! '
      f'\nМы видели твои запросы: {remote_addr.count(most_frequent(remote_addr))}')
file.close()
