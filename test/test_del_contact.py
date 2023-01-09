# -*- coding: utf-8 -*-
def test_del_first_contact(app):
    app.contact.delete_first()

    # for i in range(10):
    #     app.contact.delete_first()
    #     i -= 1
