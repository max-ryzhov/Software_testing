# -*- coding: utf-8 -*-
from model.group_param import GroupParam


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(GroupParam(group_name="test_delete"))
    app.group.modify_first_group(GroupParam(group_name="New name"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(GroupParam(group_name="test_delete2"))
    app.group.modify_first_group(GroupParam(header="New header"))
