import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"{bcolors.HEADER}This will work on unixes including OS X, Linux and Windows{bcolors.ENDC}")
print(f"{bcolors.OKBLUE}Будет работать на unixes including OS X, Linux and Windows{bcolors.ENDC}")
print(f"{bcolors.OKCYAN}This will work on unixes including OS X, Linux and Windows{bcolors.ENDC}")
print(f"{bcolors.OKGREEN}This will work on unixes including OS X, Linux and Windows{bcolors.ENDC}")
print(f"{bcolors.WARNING}This will work on unixes including OS X, Linux and Windows{bcolors.ENDC}")
print(f"{bcolors.FAIL}This will work on unixes including OS X, Linux and Windows{bcolors.ENDC}")
print(f"{bcolors.BOLD}This will work on unixes including OS X, Linux and Windows{bcolors.ENDC}")
print(f"{bcolors.UNDERLINE}This will work on unixes including OS X, Linux and Windows{bcolors.ENDC}")