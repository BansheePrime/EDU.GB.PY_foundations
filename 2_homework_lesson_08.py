#!/usr/bin/env python3
# Урок 8. Декораторы
# Задание 2
import re

# Валидация ip4 адресов через regex требует особой тщательности
# <remote_addr> "^(?:[0-9]{1,3}\.){3}[0-9]{1,3}"gm
# <request_datetime> "\[(.*?)\]"gm
# <request_type> "\"([A-Z]{3,})"gm
# <requested_resource> "(\/.{9}\/.{9})"gm ## очень плохо ориентироваться на кол-во символов
# <response_code> "\s(\d{3})\s"gm
# <response_size> "\d{3}\s(\d+)"gm

REMOTE_ADDR = re.compile(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}')
REQ_DATETIME = re.compile(r'\[(.*?)\]')
REQ_TYPE = re.compile(r'([A-Z]{3,})')
REQ_RESOURCE = re.compile(r'(\/.{9}\/.{9})')
REQ_CODE = re.compile(r'\s(\d{3})\s')
REQ_SIZE = re.compile(r'\d{3}\s(\d+)')

