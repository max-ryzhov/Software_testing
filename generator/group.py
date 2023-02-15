# -*- coding: utf-8 -*-
from model.group_construct import Group
import json
import random
import string
import os.path
import getopt
import sys


# делаем генератор параметризованным, добавляем опции -n, -f
# значения задаем в параметрах интерпритатора - edit configuration
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["numbers of groups", "file"])
except getopt.GetoptError as err:
    print(err)  # will print something like "option -a not recognized"
    getopt.usage()
    sys.exit(2)

# значение параметров генератора по умолчанию
n = 5
f = 'data/groups.json'

# обработчик значений опций -n и -f
for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == "-f":
        f = a


# генератор случайных строк
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    random_str = "".join([random.choice(symbols) for symbol in range(random.randrange(maxlen))])
    return prefix + random_str


# генератор тестовых данных
test_data_group = [Group(group_name=random_string("name_", 10),
                         header=random_string("header_", 10),
                         footer=random_string("footer_", 10)) for i in range(n)]

# записываем сгенерированные данные в f = 'data/groups.json'. indent=2 - делаем красивое отображение json
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)
with open(file, 'w') as out:
    out.write(json.dumps(test_data_group, default=lambda x: x.__dict__, indent=2))
