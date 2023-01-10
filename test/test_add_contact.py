# -*- coding: utf-8 -*-
from model.contact_param import ContactParam


def test_add_contact(app):
    app.contact.create(ContactParam(firstname="Max", lastname="Ryzhov",  middlename="Nick", nickname="max_ryzh",
                                    address="NN", company="MFI", mobile="+79997771122", email="max.ryzhov12@gmail.com",
                                    title_user='Good'))


def test_add_contact2(app):
    app.contact.create(ContactParam(firstname="Петя", lastname="Иванов", middlename="Nick", nickname="pet"))
