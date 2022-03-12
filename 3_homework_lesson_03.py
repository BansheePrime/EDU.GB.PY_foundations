#!/usr/bin/env python3
# Урок 3. Функции. Словари
names_input = ["Акакий", "Модест", "Макарий", "Никифор", "Антоний", "Варсонофий"]


def grinder(*names):
    # Операции с именами и начальными буквами
    names_initials = []
    selected_names = []

    for i in names_input:
        names_initials.append(i[0])
        names_initials = list(dict.fromkeys(names_initials))
    print(names_initials)

    for j in names_initials:
        selection = [k for k in names_input if k.startswith(names_initials[0])]
        names_initials.remove(j)
        selected_names.append(selection)
    print(selected_names)

    x = zip(names_initials, selected_names)
    print(list(x))

grinder(names_input)
