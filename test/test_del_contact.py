# -*- coding: utf-8 -*-
from model.contact_param import ContactParam


def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(ContactParam(firstname="Max", lastname="Ryzhov",  middlename="Nick", nickname="max_ryzh",
                                    address="NN", company="MFI", mobile="+79997771122", email="max.ryzhov12@gmail.com",
                                    title='Good'))
    app.contact.delete_first()
