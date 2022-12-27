# -*- coding: utf-8 -*-
def test_del_first_contact(app):
    app.session.login(user_name="admin", password="secret")
    app.contact.delete_first()
    app.session.logout()





    # i = 10
    # while i > 0:
    #     app.contact.del_first_contact()
    #     i -= 1
