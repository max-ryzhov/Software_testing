# -*- coding: utf-8 -*-
from model.contact_construct import Contact


def test_add_contact(app):
    added_contact = Contact(firstname="Max", lastname="Ryzhov", middlename="Nick", nickname="max_ryzh",
                            address="NN", company="MFI", mobile="+79997771122", email="max.ryzhov12@gmail.com",
                            title_user='Good')
    old_contacts = app.contact.get_contact_list()
    app.contact.create(added_contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(added_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)








# def test_add_contact2(app):
#     app.contact.create(ContactParam(firstname="Петя", lastname="Иванов", middlename="Nick", nickname="pet"))
#
