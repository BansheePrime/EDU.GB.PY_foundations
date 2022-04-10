#!/usr/bin/env python3
# Урок 8. Декораторы
# Задание 2
import re
import os

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
REQ_TYPE = re.compile(r'\"([A-Z]{3,})')
REQ_RESOURCE = re.compile(r'(\/.{9}\/.{9})')
REQ_CODE = re.compile(r'\s(\d{3})\s')
REQ_SIZE = re.compile(r'\d{3}\s(\d+)')


def log_parser(raw_line):
    ''' Парсер логов по схеме задания '''
    parsed_data = (REMOTE_ADDR.findall(raw_line), REQ_DATETIME.findall(raw_line), REQ_TYPE.findall(raw_line), REQ_RESOURCE.findall(raw_line), REQ_CODE.findall(raw_line), REQ_SIZE.findall(raw_line))
    clear_parsed_data = ''
    for i in parsed_data:
        clear_parsed_data = clear_parsed_data + str(i).strip('[]')
    return clear_parsed_data

# raw_line = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# print(log_parser(raw_line))
with open('nginx_logs.txt') as file:
    for line in file:
        raw_line = file.readline()
        parsed_raw = log_parser(raw_line)
        with open('parsing_nginx_logs.txt', 'a') as result:
            result.write(parsed_raw)
            result.write('\n')
