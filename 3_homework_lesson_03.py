#!/usr/bin/env python3
# Урок 3. Функции. Словари
names_input = ["Акакий", "Модест", "Макарий", "Никифор", "Антоний", "Варсонофий"]


def grinder(*names):
    # Создание тезауруса
    names_initials = []
    selected_names = []
    dict_content = {}

    for i in names_input:
        names_initials.append(i[0])
        names_initials = list(dict.fromkeys(names_initials))
    print(names_initials)

    for j in names_initials:
        selection = [k for k in names_input if k.startswith(names_initials[0])]
        names_initials.pop(0)
        selected_names.append(selection)
        dict_content.update({j: selection})
    return print(dict_content)

grinder(names_input)
