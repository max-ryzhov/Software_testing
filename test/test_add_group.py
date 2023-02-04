# -*- coding: utf-8 -*-
from model.group_construct import Group
import pytest

test_data = [Group(group_name="Meeting1", header="Hello1", footer="Bye1"),
             Group(group_name="Second", header="Hello1", footer="Bye1"),
             Group(group_name="Third", header="Hello1", footer="Bye1")]


@pytest.mark.parametrize('group', test_data)
def test_add_group(app, group):
    # old_groups = app.group.get_group_list()
    # added_group = Group(group_name="Meeting1", header="Hello1", footer="Bye1")
    app.group.create(group)
    # assert len(old_groups) + 1 == app.group.count()    # проверка по хэшу - по длине списка, без извлечения св-в
    # new_groups = app.group.get_group_list()
    # old_groups.append(added_group)
    # assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
