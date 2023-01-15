# -*- coding: utf-8 -*-
from model.contact_construct import Contact


def test_view_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Max", lastname="Ryzhov", middlename="Nick", nickname="max_ryzh",
                                   address="NN", company="MFI", mobile="+79997771122", email="max.ryzhov12@gmail.com",
                                   title='Good'))
    app.contact.view_first()
