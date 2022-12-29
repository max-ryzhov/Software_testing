# -*- coding: utf-8 -*-
def test_view_first_contact(app):
    app.session.login(user_name="admin", password="secret")
    app.contact.view_first()
    app.session.logout()
