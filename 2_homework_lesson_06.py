#!/usr/bin/env python3
# Разбор решения преподавателя.
# Работает сильно быстрее моего решения.
with open('nginx_logs.txt') as file:
    data = []
    spam_dict = {}
    for line in file:
        cleaning = line.split()
        data.append((cleaning[0], cleaning[5].replace('"', ''), cleaning[6]))
        spam_dict.setdefault(cleaning[0], 0)
        spam_dict[cleaning[0]] += 1

spam_dict = sorted(spam_dict.items(), key=lambda x: x[1], reverse=True)
print(f'Трое кандидатов на проверку: {spam_dict[:3]}')
