#!/usr/bin/env python3
# Разбор решения преподавателя

import os
import shutil

target_directory = 'task3'
if not os.path.exists(target_directory):
    os.mkdir(target_directory)

good_folder = r'my_project'
files = []

for r, d, f in os.walk(good_folder):
    for file in f:
        if '.html' in file:
            files.append(os.path.join(r, file))
for path in files:
    newest_folder = os.path.join(my_dir, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(newest_folder):
        os.mkdir(newest_folder)
    save_path = os.path.join(newest_folder, os.path.basename(path))
    shutil.copy(path, save_path)
