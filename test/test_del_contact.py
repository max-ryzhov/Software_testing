# -*- coding: utf-8 -*-
from model.contact_param import ContactParam


def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(ContactParam(firstname="test_delete", lastname="test_delete2"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []    # delete elem[0]
    assert old_contacts == new_contacts
