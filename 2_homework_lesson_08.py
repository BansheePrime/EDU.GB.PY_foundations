#!/usr/bin/env python3
# Урок 8. Декораторы
# Задание 2
import re

# Валидация ip4 адресов через regex требует особой тщательности
# <remote_addr> "^(?:[0-9]{1,3}\.){3}[0-9]{1,3}"gm
# <request_datetime>
# <request_type> "[A-Z]{3,}\s"gm
# <requested_resource>
# <response_code>
# <response_size>