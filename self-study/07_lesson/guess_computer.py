  GNU nano 5.6.1                                       guess_computer.py                                                 #!/usr/bin/env python3

number = 50
proper = [0, 1, 2]
move = 0

guess = int(input(f'Я попробую угадать ваше число. Вы загадали {number}? Нажмите "2", если я угадала. \nНажмите "1", есл>while guess not in proper:
        guess = int(input(f'Вы набрали {guess}. Я ждала от вас 0, 1 или 2. Попробуйте еще раз: '))

if guess == 2:
        # print('Начнём угадывать ваше число.')
        print(f'Я отгадала! Вы загадали {number}.')

elif guess == 1:
        print(f'Значит ваше число больше {number}? Хм, надо подумать ...')
        number = (100 - number)//2 + number
        guess = int(input(f'Я попробую угадать ваше число. Вы загадали {number}? Нажмите "2", если я угадала. \nНажмите >
elif guess ==0:
        print(f'Значит ваше число меньше {number}? Хм, надо подумать ...')

else:
        print('Thank you!')

print(guess)
print(number)
