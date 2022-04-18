#!/usr/bin/env python3
# Урок 10. Объектно-ориентированное программирование. Продвинутый уровень
# Задание 1
# разбор решения преподавателя
class Matrix:
    def __init__(self, input_data):
        self.input = input_data

    def __str__(self):
        return '\n\\'.join([' '.join(map(str, line)) for line in self.input])

    def __add__(self, other):
        answer = ''
        if len(self.input) == len(other.input):
            for line_1, line_2 in zip(self.input, other.input):
                if len(line_1) != len(line_2):
                    return "Please, check the shapes forms"

                summed_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join(map(str, summed_line)) + '\n'
        else:
            return "Please, check the shapes forms"
        return answer

matrix_1 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
matrix_2 = Matrix([[2, 3], [4, 5], [6, 7], [10, 20]])
print(matrix_1)
print()