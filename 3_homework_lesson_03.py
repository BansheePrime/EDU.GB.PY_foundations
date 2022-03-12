#!/usr/bin/env python3
# Урок 3. Функции. Словари
'''
Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
Например:
>>>  thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"], "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки?
Как поступить, если потребуется сортировка по ключам? Можно ли использовать словарь в этом случае?
'''
names_input = ("Акакий", "Модест", "Макарий", "Никифор", "Антоний", "Варсонофий")


def grinder(*names):
    # Операции с именами и начальными буквами
    names_initials = []
    dict_content = []
    dict_values = []
    dict_names = {}

    for i in names_input:
        names_initials.append(i[0])
        # names_initials = list(dict.fromkeys(names_initials))
    print(names_initials)

    dict_content = zip(names_initials, names_input)
    print(tuple(dict_content))
    x = tuple(dict_content.count('А'))
    print(x)

# def softer(ini_list, inp_names):
#     return
    # for j in names_initials:
    #     print(x for x in names_input if j.startswith(names_initials))
    #
    #     dict_values = [x for x in names_input if x is ]
    #     if i.startswith(i[0]):
    #         dict_values.append(i)


    # for j_letter, j_name in zip(dict_keys, dict_values):
    #     dict_names.update({j_letter: j_name})
    #     print(j_letter, j_name)
    # print(dict_names)

grinder(names_input)
