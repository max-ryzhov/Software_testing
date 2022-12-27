# -*- coding: utf-8 -*-
def test_del_first_contact(app):
    app.session.login(user_name="admin", password="secret")
    app.contact.del_first_contact()
    app.session.logout()
