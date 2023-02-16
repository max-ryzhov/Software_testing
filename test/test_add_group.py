# -*- coding: utf-8 -*-
from model.group_construct import Group


# from data.add_group import constant as test_data_group
# from data.groups import test_data_group
# import pytest


# # генератор случайных строк
# def random_string(prefix, maxlen):
#     symbols = string.ascii_letters + string.digits
#     random_str = "".join([random.choice(symbols) for symbol in range(random.randrange(maxlen))])
#     return prefix + random_str
#
#
# # генератор тестовых данных
# test_data_group = [Group(group_name=random_string("name_", 10),
#                          header=random_string("header_", 10),
#                          footer=random_string("footer_", 10)) for i in range(1)]


# # название параметра, в кот. передаются данные; тестовые данные; строковое представление данных для отчета;
# @pytest.mark.parametrize('group', test_data_group, ids=[str(x) for x in test_data_group])
# def test_add_group(app, group):

# вариант реализации - динамическое связывание тестовых функций(теста) и тестовых данных с помощью фикстуры data_groups
def test_add_group(app, data_groups):
    group = data_groups
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()  # сначала проверка по хэшу - по длине списка, без извлечения св-в
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)





    # генератор тестовых наборов
    # test_data = [Group(group_name=name, header=header, footer=footer)
    #              for name in ["", random_string("name_", 10)]
    #              for header in ["", random_string("header_", 10)]
    #              for footer in ["", random_string("footer_", 10)]
    #              ]
