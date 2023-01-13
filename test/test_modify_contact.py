# -*- coding: utf-8 -*-
from model.contact_param import ContactParam


def test_update_contact(app):
    if app.contact.count() == 0:
        app.contact.create(ContactParam(firstname="Default", lastname="User", address="for_modification"))
    mod_contact = ContactParam(firstname="Max", lastname="Ryzhov",  middlename="Nick", nickname="max_ryzh",
                                    address="NN", company="MFI", mobile="+79997771122", email="max.ryzhov12@gmail.com",
                                    title_user='Good')
    old_contacts = app.contact.get_contact_list()
    app.contact.update_first(mod_contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
