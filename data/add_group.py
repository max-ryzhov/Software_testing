# -*- coding: utf-8 -*-
from model.group_construct import Group
import random
import string

# константные данные
constant = [
    Group(group_name='1name_const', header='1header_const', footer='1footer_const'),
    Group(group_name='2name_const', header='2header_const', footer='2footer_const')
]


# генератор случайных строк
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    random_str = "".join([random.choice(symbols) for symbol in range(random.randrange(maxlen))])
    return prefix + random_str


# генератор тестовых данных
test_data_group = [Group(group_name=random_string("name_", 10),
                         header=random_string("header_", 10),
                         footer=random_string("footer_", 10)) for i in range(1)]
