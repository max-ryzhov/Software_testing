# -*- coding: utf-8 -*-
from random import randrange
from model.contact_construct import Contact


def test_update_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Default", lastname="User", address="for_modification"))
    mod_contact = Contact(firstname="mod_name", lastname="mod_lastname", address="mod_address", mobile="+0000",
                          email="mod@gmail.com", title_user='Good')
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    mod_contact.cont_id = old_contacts[index].cont_id    # записываю в мод.группу ID старой группы с веб-страницы
    app.contact.modify_contact_by_index(index, mod_contact)
    assert len(old_contacts) == app.contact.count()
    mod_contacts = app.contact.get_contact_list()
    old_contacts[index] = mod_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(mod_contacts, key=Contact.id_or_max)
