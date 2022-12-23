# -*- coding: utf-8 -*-
import pytest
from group_param import GroupParam
from application.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(user_name="admin", password="secret")
    app.create_new_group(GroupParam(group_name="Meeting", header="Hello", footer="Bye"))
    app.logout()


def test_add_empty_group(app):
    app.login(user_name="admin", password="secret")
    app.create_new_group(GroupParam(group_name="", header="", footer=""))
    app.logout()
