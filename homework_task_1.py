#!/usr/bin/env python3
# How long in took you?

duration = int(input('Введите время в секундах для пересчета: '))
print(f'Вы ввели {duration} сек.\nПодумаешь, бином Ньютона!\n ')
days = hours = minutes = seconds = 0

days = duration // 86400
hours = (duration - (days * 86400)) // 3600
minutes = (duration - (days * 86400) - (hours * 3600)) // 60
seconds = (duration - (days * 86400) - (hours * 3600) - (minutes * 60))

print(f'{days} дн {hours} час {minutes} мин {seconds} сек')
