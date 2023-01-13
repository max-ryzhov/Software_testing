# -*- coding: utf-8 -*-
from model.contact_param import ContactParam


def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(ContactParam(firstname="test_delete", lastname="test_delete2"))
    old_contacts = app.contact.get_contact_list()
    print(old_contacts)
    app.contact.delete_first()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)

    # old_contacts[0:1] = []    # delete elem[0]
    # assert old_contacts == new_contacts



# def test_delete_first_group(app):
#     if app.group.count() == 0:
#         app.group.create(GroupParam(group_name="test_delete"))
#     old_groups = app.group.get_group_list()
#     app.group.delete_first()
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) - 1 == len(new_groups)
#     old_groups[0:1] = []    # delete elem[0]
#     assert old_groups == new_groups