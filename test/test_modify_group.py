# -*- coding: utf-8 -*-
from model.group_construct import Group


def test_modify_group_name(app):
    mod_group = Group(group_name="Modified name")    # назвал модифицированную группу mod_group
    if app.group.count() == 0:    # если групп нет, то создать
        app.group.create(Group(group_name="For modify"))
    old_groups = app.group.get_group_list()    # сохранил список групп до модификации
    mod_group.group_id = old_groups[0].group_id    # по умолчанию id в mod_group - None. Присваиваю id 1й группы.
    app.group.modify_first_group(mod_group)    # модифицирую 1ю группу
    new_groups = app.group.get_group_list()  # подтягиваю фактический список групп с веб станицы после модификации
    assert len(old_groups) == len(new_groups)
    old_groups[0] = mod_group    # формирую список путем замены 1й группы старого списка на mod_group
    # сравниваем список, "какой должен быть по коду", с фактическим списком с веб страницы
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_name2(app):
    if app.group.count() == 0:    # если групп нет, то создать
        app.group.create(Group(group_name="For modify2"))
    old_groups = app.group.get_group_list()
    # Сразу передаю id 1й групп в конструктор mod_group
    mod_group = Group(group_name="Second modification", group_id=old_groups[0].group_id)
    app.group.modify_first_group(mod_group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = mod_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
#
#

