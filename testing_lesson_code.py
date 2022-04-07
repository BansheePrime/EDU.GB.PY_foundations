#!/usr/bin/env python3
import os

folder = '/home/gidra/learning_python/EDU.GB.PY_foundations/'
search_result = [file for file in os.listdir(folder) if file.lower().endswith('.py')]
print(search_result)

print()
py_files = [os.path.join(folder, item) for item in os.listdir(folder) if item.lower().endswith('.py')]
print(py_files)

print()
dj_folder = '/home/gidra/.local/share/virtualenvs/self-study_EDU.GB.foundations.02.2022-7qDhcPcq/lib/python3.8/site-packages/django/'
django_dirs = [counter for counter in os.listdir(dj_folder) if os.path.isdir(os.path.join(dj_folder, counter))]
print(django_dirs)

print()
