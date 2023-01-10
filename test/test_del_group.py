# -*- coding: utf-8 -*-
from model.group_param import GroupParam


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(GroupParam(group_name="test_delete"))
    app.group.delete_first()

    # for i in range(10):
    #     app.group.delete_first()
    #     i -= 1