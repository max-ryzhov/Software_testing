# -*- coding: utf-8 -*-
from random import randrange
from model.group_construct import Group


def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test_delete"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []    # delete elem[0]
    assert old_groups == new_groups
