#!/usr/bin/env python3
# Урок 8. Декораторы
# Задание 2
import re

# Валидация ip4 адресов через regex требует особой тщательности
# <remote_addr> "^(?:[0-9]{1,3}\.){3}[0-9]{1,3}"gm
# <request_datetime> "\[(.*?)\]"g
# <request_type> "[A-Z]{3,}\s"gm "\"[A-Z]{3,}"g #второй ааприант лучше
# <requested_resource> "(\/.{9}/.{9})"g ## очень плохно ориентироваться на кол-во символов здесь
# <response_code> "\s\d{3}\s"gm
# <response_size> "(\s\d{3}\s\d+)"gm ## потом взять только вторую часть