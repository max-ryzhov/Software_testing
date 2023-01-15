# -*- coding: utf-8 -*-
from random import randrange
from model.group_construct import Group


def test_modify_group_name(app):
    mod_group = Group(group_name="Modified name")
    if app.group.count() == 0:
        app.group.create(Group(group_name="For modify"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    mod_group.group_id = old_groups[index].group_id    # по умолчанию id в mod_group - None. Присваиваю id 1й группы.
    app.group.modify_group_by_index(index, mod_group)    # модифицирую 1ю группу
    assert len(old_groups) == app.group.count()    # кол-во групп не изменилось

    new_groups = app.group.get_group_list()  # подтягиваю фактический список групп с веб станицы после модификации
    old_groups[index] = mod_group    # формирую список путем замены 1й группы старого списка на mod_group
    # сравниваем список, "какой должен быть по коду", с фактическим списком с веб страницы
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_name2(app):
    mod_group = Group(group_name="Second modification")
    if app.group.count() == 0:
        app.group.create(Group(group_name="For modify2"))
    old_groups = app.group.get_group_list()
    mod_group.group_id = old_groups[0].group_id
    app.group.modify_first_group(mod_group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = mod_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


