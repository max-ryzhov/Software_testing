# -*- coding: utf-8 -*-
from model.contact_param import ContactParam


def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(ContactParam(firstname="Max", lastname="Ryzhov",  middlename="Nick", nickname="max_ryzh",
                                    address="NN", company="MFI", mobile="+79997771122", email="max.ryzhov12@gmail.com",
                                    title='Good'))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)


# def test_delete_first_group(app):
#     if app.group.count() == 0:
#         app.group.create(GroupParam(group_name="test_delete"))
#     old_groups = app.group.get_group_list()
#     app.group.delete_first()
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) - 1 == len(new_groups)
#     old_groups[0:1] = []    # delete elem[0]
#     assert old_groups == new_groups