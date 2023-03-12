# -*- coding: utf-8 -*-
from model.group_construct import Group


# вариант реализации - динамическое связывание тестовых функций(теста) и тестовых данных с помощью фикстуры json_groups
def test_add_group(app, db, json_groups):
    group = json_groups
    old_groups = db.get_group_list()    # список групп загружаем из db
    app.group.create(group)
    new_groups = db.get_group_list()    # новый список групп загружаем из db
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
