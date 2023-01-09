# -*- coding: utf-8 -*-
from model.group_param import GroupParam


def test_modify_group_name(app):
    app.group.modify_first_group(GroupParam(group_name="New name"))


def test_modify_group_header(app):
    app.group.modify_first_group(GroupParam(header="New header"))
