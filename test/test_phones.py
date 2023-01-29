import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_hp == merge_phones_like_on_homepage(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)  # что заменять (скобки пробел минус) /на что заменять (на пустоту)
    # /где заменять(в строке)


def merge_phones_like_on_homepage(contact):
    return '\n'.join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.homephone, contact.mobilephone,
                                                               contact.workphone, contact.secondphone]))))
