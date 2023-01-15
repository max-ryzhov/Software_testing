# -*- coding: utf-8 -*-
from model.contact_param import ContactParam


def test_update_contact(app):
    if app.contact.count() == 0:
        app.contact.create(ContactParam(firstname="Default", lastname="User", address="for_modification"))
    mod_contact = ContactParam(firstname="mod_name", lastname="mod_lastname", address="mod_address", mobile="+0000",
                               email="mod@gmail.com", title_user='Good')
    old_contacts = app.contact.get_contact_list()
    mod_contact.cont_id = old_contacts[0].cont_id    # записываю ID в мод.группу с веб-страницы
    app.contact.update_first(mod_contact)
    mod_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(mod_contacts)
    old_contacts[0] = mod_contact
    assert sorted(old_contacts, key=ContactParam.id_or_max) == sorted(mod_contacts, key=ContactParam.id_or_max)


