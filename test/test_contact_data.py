import re


def test_compare_view_and_edit_form(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_hp == merge_phones_like_on_homepage(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_hp == merge_emails_like_on_homepage(contact_from_edit_page)
    # firstname/lastname добавил clear (в firstname ругается, если на edit_page пробел сзади)
    assert clear(contact_from_home_page.firstname) == clear(contact_from_edit_page.firstname)
    assert clear(contact_from_home_page.lastname) == clear(contact_from_edit_page.lastname)
    assert contact_from_home_page.address == contact_from_edit_page.address


def clear(s):
    return re.sub("[() -]", "", s)  # что заменять (скобки пробел минус) /на что заменять (на пустоту)
    # /где заменять(в строке)


def merge_phones_like_on_homepage(contact):
    return '\n'.join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.homephone, contact.mobilephone,
                                                               contact.workphone, contact.secondphone]))))


def merge_emails_like_on_homepage(contact):
    return '\n'.join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.email, contact.email2,
                                                               contact.email3]))))
