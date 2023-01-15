# -*- coding: utf-8 -*-
from model.group_construct import GroupConstruct


def test_add_group(app):
    old_groups = app.group.get_group_list()
    added_group = GroupConstruct(group_name="Meeting1", header="Hello1", footer="Bye1")
    app.group.create(added_group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(added_group)
    assert sorted(old_groups, key=GroupConstruct.id_or_max) == sorted(new_groups, key=GroupConstruct.id_or_max)


def test_add_second_group(app):
    old_groups = app.group.get_group_list()
    added_group = GroupConstruct(group_name="1", header="2", footer="3")
    app.group.create(added_group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(added_group)
    assert sorted(old_groups, key=GroupConstruct.id_or_max) == sorted(new_groups, key=GroupConstruct.id_or_max)
