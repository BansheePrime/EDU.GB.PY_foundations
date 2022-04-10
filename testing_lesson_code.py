import time

# def countdown(t):
#     real = t
#     while t > 0:
#         CURSOR_UP = '\033[F'
#         ERASE_LINE = '\033[K'
#         if t == real:
#             print(ERASE_LINE + 'Duration : {}s'.format(t))
#         else:
#             print(CURSOR_UP + ERASE_LINE + 'Duration : {}s'.format(t))
#         time.sleep(1)
#         t -= 1
#
# countdown(4)

# for n in range(5):
#     print('\r', n, end='')
#     time.sleep(1)


for i in range(7, -1, -1):
    time.sleep(1)
    print(f'\r{i}', end='')

