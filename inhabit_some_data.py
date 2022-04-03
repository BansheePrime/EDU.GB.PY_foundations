#!/usr/bin/env python3
# Скрипт из методички к уроку.
# Создаёт в папке some_data 1000 небольших файлов разного размера.
import os
import random

folder = 'some_data'
letters = [chr(code) for code in range(ord('a'), ord('z') + 1)]

for _ in range(100 ** 3):
	f_name = ''.join(random.sample(letters, random.randit(5, 10)))
	f_content = bytes(random.randint(0, 255)
		for _ in range(random.randrange(10 ** 5)))

	with open(os.path.join(folder, f'{f_name}.bin'), 'wb') as f:
		f.write(f_content)

