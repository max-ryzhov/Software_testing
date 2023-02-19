# -*- coding: utf-8 -*-
from model.contact_construct import Contact
import jsonpickle
import random
import string
import os.path
import getopt
import sys


# делаем генератор параметризованным, добавляем опции -n, -f
# значения задаем в параметрах интерпритатора - edit configuration
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["numbers of contact", "file"])
except getopt.GetoptError as err:
    print(err)  # will print something like "option -a not recognized"
    getopt.usage()
    sys.exit(2)

# значение параметров генератора по умолчанию
n = 3
f = 'data/contacts.json'

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
test_data_contact = [Contact(firstname=random_string('firstname_', 7),
                             lastname=random_string('lastname_', 7),
                             nickname=random_string('nickname_', 7),
                             address=random_string('address_', 7),
                             company=random_string('company_', 7),
                             email=random_string('email_', 7),
                             email2=random_string('email2_', 7),
                             email3=random_string('email3_', 7),
                             mobilephone=random_string('mobilephone_', 7),
                             homephone=random_string('homephone_', 7),
                             secondphone=random_string('secondphone_', 7)) for i in range(n)]


# записываем сгенерированные данные в f = 'data/contacts.json'. indent=2 - делаем красивое отображение json
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)
with open(file, 'w') as out:
    jsonpickle.set_encoder_options('json', indent=2)
    out.write(jsonpickle.encode(test_data_contact))
