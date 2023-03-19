# -*- coding: utf-8 -*-
import random
from model.contact_construct import Contact


def test_del_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test_delete", lastname="test_delete2"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)

    app.contact.delete_contact_by_id(contact.cont_id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
