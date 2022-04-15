class TermColoring:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    col_off = '\033[0m'

print(f"{TermColoring.HEADER}This will work on unixes including OS X, Linux and Windows{TermColoring.col_off}")
print(f"{TermColoring.OKBLUE}Будет работать на unixes including OS X, Linux and Windows{TermColoring.col_off}")
print(f"{TermColoring.OKCYAN}This will work on unixes including OS X, Linux and Windows{TermColoring.col_off}")
print(f"{TermColoring.OKGREEN}This will work on unixes including OS X, Linux and Windows{TermColoring.col_off}")
print(f"{TermColoring.WARNING}This will work on unixes including OS X, Linux and Windows{TermColoring.col_off}")
print(f"{TermColoring.FAIL}This will work on unixes including OS X, Linux and Windows{TermColoring.col_off}")
print(f"{TermColoring.BOLD}This will work on unixes including OS X, Linux and Windows{TermColoring.col_off}")
print(f"{TermColoring.UNDERLINE}This will work on unixes including OS X, Linux and Windows{TermColoring.col_off}")
