# -*- coding: utf-8 -*-
def test_delete_first_group(app):
    app.session.login(user_name="admin", password="secret")    # .session т.к. login перенесли в fixture.session
    app.group.delete_first()
    app.session.logout()


    # for i in range(10):
    #     app.group.delete_first()
    #     i -= 1