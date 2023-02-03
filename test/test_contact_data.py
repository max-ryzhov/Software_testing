# -*- coding: utf-8 -*-
from random import randrange
import re


def test_compare_view_and_edit_form(app):
    # выбор случайного контакта
    contacts = app.contact.get_contact_list()
    random_id = randrange(len(contacts))
    # проверка контакта
    contact_from_home_page = app.contact.get_contact_list()[random_id]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(random_id)
    assert contact_from_home_page.all_phones_from_hp == merge_phones_like_on_homepage(contact_from_edit_page)
    assert clear_spaces(contact_from_home_page.all_emails_from_hp) == merge_emails_like_on_homepage(
        contact_from_edit_page)
    # firstname/lastname добавил clear (в firstname ругается, если на edit_page пробел сзади)
    assert clear_spaces(contact_from_home_page.firstname) == clear_spaces(contact_from_edit_page.firstname)
    assert clear_spaces(contact_from_home_page.lastname) == clear_spaces(contact_from_edit_page.lastname)
    assert contact_from_home_page.address == contact_from_edit_page.address
    print()
    print(random_id, contact_from_home_page, contact_from_edit_page)


def clear_phones(s):
    return re.sub("[() -]", "", s)  # что заменять (скобки пробел минус) /на что заменять (на пустоту)
    # /где заменять(в строке)


def clear_spaces(s):
    return re.sub("[ ]", "", s)


def merge_phones_like_on_homepage(contact):
    return '\n'.join(filter(lambda x: x != "",
                            map(lambda x: clear_phones(x),
                                filter(lambda x: x is not None, [contact.homephone, contact.mobilephone,
                                                                 contact.workphone, contact.secondphone]))))


def merge_emails_like_on_homepage(contact):
    return '\n'.join(filter(lambda x: x != "",
                            map(lambda x: clear_spaces(x),
                                filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))
