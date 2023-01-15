# -*- coding: utf-8 -*-
from model.group_construct import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    added_group = Group(group_name="Meeting1", header="Hello1", footer="Bye1")
    app.group.create(added_group)
    assert len(old_groups) + 1 == app.group.count()    # проверка по хэшу - по длине списка, без извлечения св-в
    new_groups = app.group.get_group_list()
    old_groups.append(added_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
