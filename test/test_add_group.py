# -*- coding: utf-8 -*-
from model.group_param import GroupParam


def test_add_group(app):
    app.session.login(user_name="admin", password="secret")    # .session т.к. login перенесли в fixture.session
    app.group.create(GroupParam(group_name="Meeting1", header="Hello1", footer="Bye1"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(user_name="admin", password="secret")
    app.group.create(GroupParam(group_name="1", header="2", footer="3"))
    app.session.logout()
