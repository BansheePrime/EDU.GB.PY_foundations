#!/usr/bin/env python3
random_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = random_list[0:1]
for i in range(len(random_list) - 1):
    # print (random_list[i], random_list[i + 1])
    if random_list[i] < random_list[i + 1]:
        result_list.append(random_list[i + 1])

print(result_list[1:])
