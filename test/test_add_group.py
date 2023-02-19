# -*- coding: utf-8 -*-
from model.group_construct import Group


# вариант реализации - динамическое связывание тестовых функций(теста) и тестовых данных с помощью фикстуры json_groups
def test_add_group(app, json_groups):
    group = json_groups
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()  # сначала проверка по хэшу - по длине списка, без извлечения св-в
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
