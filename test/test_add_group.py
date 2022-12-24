# -*- coding: utf-8 -*-
import pytest
from model.group_param import GroupParam
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(user_name="admin", password="secret")    # .session т.к. login перенесли в fixture.session
    app.create_new_group(GroupParam(group_name="Meeting", header="Hello", footer="Bye"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(user_name="admin", password="secret")
    app.create_new_group(GroupParam(group_name="", header="", footer=""))
    app.session.logout()
