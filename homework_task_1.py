#!/usr/bin/env python3
# How long in took you?

duration = int(input('Введите время в секундах для пересчета: '))
print(f'Вы ввели {duration} сек.\n Подумаешь, бином Ньютона!\n ')
days = hours = minutes = seconds = 0

if duration // 60 < 1:
    print(f'{duration} сек. Это много или мало?')
elif 1 < (duration // 60) < 61:
    minutes = duration // 60 
    seconds = duration - (minutes * 60)
    print(f'{minutes} мин и {seconds} сек.')
elif 60 < (duration // 60) < 3601:
    hours = duration // 360 ## ДОПИСАТЬ
    minutes = duration // 60 ## ДОПИСАТЬ
    seconds = duration - (minutes * 60)
    print(f'{hours} час {minutes} мин {seconds} сек.')
elif 60 < (duration // 60) < 3601:
    days = duration // 3600 ## ДОПИСАТЬ
    hours = duration // 360 ## ДОПИСАТЬ
    minutes = duration // 60 ## ДОПИСАТЬ
    seconds = duration - (minutes * 60)
    print(f'{days} дн {hours} час {minutes} мин {seconds} сек.')
else:
    print(f'Извините, вы сказали {duration}. Хм, тут нужен суперкомпьютер, извините.')
