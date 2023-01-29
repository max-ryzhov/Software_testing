# -*- coding: utf-8 -*-
from random import randrange
from model.contact_construct import Contact


def test_view_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Max", lastname="Ryzhov", middlename="Nick", nickname="max_ryzh",
                                   address="NN", company="MFI", mobilephone="+79997771122",
                                   email="max.ryzhov12@gmail.com"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.view_contact_by_index(index)
