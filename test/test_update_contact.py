# -*- coding: utf-8 -*-
from model.contact_param import ContactParam


def test_update_contact(app):
    app.session.login(user_name="admin", password="secret")
    app.contact.update_first(ContactParam(firstname="Alex", lastname="Medved", nickname="medved", address="NN",
                                    company="MFI", mobile="+79997770000", email="medved12@gmail.com",
                                    middlename="Ser", title='Good'))
    app.session.logout()
