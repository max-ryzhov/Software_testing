# -*- coding: utf-8 -*-
from model.contact_param import ContactParam


def test_update_contact(app):
    app.session.login(user_name="admin", password="secret")
    app.contact.update_first(ContactParam(firstname="Alex", lastname="Medved", nickname="medved", address="NN",
                                    company="MFI", mobile="+79997770000", email="medved12@gmail.com",
                                    middlename="Ser", title='Good'))
    app.session.logout()









# def test_add_contact2(app):
#     app.session.login(user_name="admin", password="secret")
#     app.contact.create(ContactParam(firstname="Петя", lastname="Иванов", nickname="pet", address="Spb",
#                                     company="Ya", mobile="+79993330011", email="pet@gmail.com",
#                                     middlename="Ya"))
#     app.session.logout()
