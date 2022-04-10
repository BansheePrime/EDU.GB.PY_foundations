#!/usr/bin/env python3
# Урок 8. Декораторы
# Задание 2
import re

# Валидация ip4 адресов через regex требует особой тщательности
# https://regex101.com/
# <remote_addr> "^(?:[0-9]{1,3}\.){3}[0-9]{1,3}"gm
# <request_datetime> "\[(.*?)\]"gm
# <request_type> "\"([A-Z]{3,})"gm
# <requested_resource> "(\/.{9}\/.{9})"gm ## очень плохо ориентироваться на кол-во символов
# <response_code> "\s(\d{3})\s"gm
# <response_size> "\d{3}\s(\d+)"gm
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')

REMOTE_ADDR = re.compile(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}')
REQ_DATETIME = re.compile(r'\[(.*?)\]')
REQ_TYPE = re.compile(r'([A-Z]{3,})')
REQ_RESOURCE = re.compile(r'(\/.{9}\/.{9})')
REQ_CODE = re.compile(r'\s(\d{3})\s')
REQ_SIZE = re.compile(r'\d{3}\s(\d+)')


def log_parser(raw_line):
