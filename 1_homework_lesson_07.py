#!/usr/bin/env python3
# Разбор решения преподавателя

import os

structure = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
for start_dir, other_dirs in structure.items():
    if os.path.exists(start_dir):
        print(f'Существует {start_dir}')
    else:
        for one_dir in other_dirs:
            current_dir = os.path.join(start_dir, one_dir)
            os.makedirs(current_dir)
