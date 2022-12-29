# -*- coding: utf-8 -*-
from model.group_param import GroupParam


def test_add_group(app):
    app.session.login(user_name="admin", password="secret")    # .session т.к. login перенесли в fixture.session
    app.group.update_first(GroupParam(group_name="Meeting22", header="Hello33", footer="Bye44"))
    app.session.logout()
