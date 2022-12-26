# -*- coding: utf-8 -*-
from model.contact_param import ContactParam


def test_add_contact(app):
    app.session.login(user_name="admin", password="secret")
    app.contact.create(ContactParam(firstname="Max", lastname="Ryzhov", nickname="max_ryzh", address="NN",
                                    company="MFI", mobile="+79997771122", email="max.ryzhov12@gmail.com",
                                    middlename="Nick"))
    app.session.logout()


def test_add_contact2(app):
    app.session.login(user_name="admin", password="secret")
    app.contact.create(ContactParam(firstname="Петя", lastname="Иванов", nickname="pet", address="Spb",
                                    company="Ya", mobile="+79993330011", email="pet@gmail.com",
                                    middlename="Ya"))
    app.session.logout()
