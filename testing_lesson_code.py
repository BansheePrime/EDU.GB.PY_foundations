# letters = {chr(code) for code in range(ord('а'), ord('я') + 1)}
# letters.add('ё')
# print(type(letters), str(len(letters)), letters)

# def name_is_valid(name):
#     if not name or set(name.lower()) - letters:
#         return False

# name = ['абырвалг', 'monster', 'авыqwe']
# for i in name:
#     result = set(str(name)) - letters
#     print(result)

valid_letters = {chr(sym_code) for sym_code in range(ord('а'), ord('я') + 1)}
valid_letters.add('ё')

def name_is_valid(name):
    if not name or set(name.lower()) - set(valid_letters):
        return False
    return name.istitle()

if __name__ == '__main__':
    while True:
        name = input('Введите имя:\n')
        if name_is_valid(name):
            break
    print(f'пользователь: {name}')
