# -*- coding: utf-8 -*-
import random
from model.group_construct import Group


def test_delete_some_group(app, db):
    if len(db.get_group_list()) == 0:    # длина списка групп из db
        app.group.create(Group(group_name="test_delete"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_by_id(group.group_id)    # перещли на удаление групп по group_id
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == app.group.count()
    old_groups.remove(group)
    assert old_groups == new_groups
