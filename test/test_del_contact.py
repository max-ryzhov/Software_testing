# -*- coding: utf-8 -*-
from model.contact_param import ContactParam


def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(ContactParam(firstname="test_delete", lastname="test_delete2"))
    old_contacts = app.contact.get_contact_list()
    print()
    print('old1', old_contacts)
    app.contact.delete_first()
    new_contacts = app.contact.get_contact_list()
    print('new', new_contacts)
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []    # delete elem[0]
    print('old2', old_contacts)
    assert old_contacts == new_contacts
