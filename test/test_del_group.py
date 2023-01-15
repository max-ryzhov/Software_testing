# -*- coding: utf-8 -*-
from model.group_construct import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(group_name="test_delete"))
    old_groups = app.group.get_group_list()
    app.group.delete_first()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []    # delete elem[0]
    assert old_groups == new_groups



    




    # for i in range(10):
    #     app.group.delete_first()
    #     i -= 1