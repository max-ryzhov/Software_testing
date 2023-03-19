# -*- coding: utf-8 -*-
import random
from model.group_construct import Group


def test_modify_group(app, db):    # передаем фикстуру db в кач параметра
    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name="For modify"))

    mod_group = Group(group_name="Modified name6", header='Mod_header6', footer='Mod_footer6')    # new_group_param
    # загрузил начальный список групп из БД
    old_groups = db.get_group_list()
    # выбрал рандомную группу для модификации
    group = random.choice(old_groups)
    # сохранил id и индекс выбранной группы
    mod_group_id = group.group_id
    mod_group_index = old_groups.index(group)
    # модифицировал группу в браузере по id
    app.group.modify_group_by_id(mod_group_id, mod_group)
    # вернул модифицированной группе id-шник
    mod_group.group_id = mod_group_id
    # загрузил обновленный список из БД
    new_groups = db.get_group_list()
    # заменил в старом списке начальную группу на модифицированную по mod_group_index
    old_groups[mod_group_index] = mod_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
