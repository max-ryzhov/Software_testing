# -*- coding: utf-8 -*-
from model.contact_construct import ContactConstruct
from model.group_construct import GroupConstruct


def test_add_contact_to_group(app):
    if app.contact.count() == 0:
        app.contact.create(ContactConstruct(firstname="Max", lastname="Ryzhov", middlename="Nick", nickname="max_ryzh",
                                            address="NN", company="MFI", mobile="+79997771122", email="max.ryzhov12@gmail.com",
                                            title_user='Good'))
    elif app.group.count() == 0:
        app.group.create(GroupConstruct(group_name="test_delete"))
    app.contact.add_to_group()