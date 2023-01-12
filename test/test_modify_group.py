# -*- coding: utf-8 -*-
from model.group_param import GroupParam


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(GroupParam(group_name="test_delete"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(GroupParam(group_name="New name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(GroupParam(group_name="test_delete2"))
    app.group.modify_first_group(GroupParam(header="New header"))
