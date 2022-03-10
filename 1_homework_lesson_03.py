#!/usr/bin/env python3
# Урок 3. Функции. Словари
dictionary_words = {
    'zero': 'Ноль',
    'one': 'Один',
    'two': 'Два',
    'three': 'Три',
    'four': 'Четыре',
    'five': 'Пять',
    'six': 'Шесть',
    'seven': 'Семь',
    'eight': 'Восемь',
    'nine': 'Девять',
    'ten': 'Десять'
}
word_input = input('Введите, пожалуйста, словом число от 0 до 10 на английском языке: ')


def num_translate():
    # Перевод числительных на английский язык
    return print(f'\"{dictionary_words.get(word_input, None)}\"')


num_translate()
