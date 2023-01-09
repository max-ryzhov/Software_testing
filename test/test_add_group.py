# -*- coding: utf-8 -*-
from model.group_param import GroupParam


def test_add_group(app):
    app.group.create(GroupParam(group_name="Meeting1", header="Hello1", footer="Bye1"))


def test_add_empty_group(app):
    app.group.create(GroupParam(group_name="1", header="2", footer="3"))
