# -*- coding: utf-8 -*-
from random import randrange
from model.contact_construct import Contact


def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_delete", lastname="test_delete2"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []    # delete elem[0]
    assert old_contacts == new_contacts
