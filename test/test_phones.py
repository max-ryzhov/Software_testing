import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(0)
    assert contact_from_home_page.homephone == clear(contact_from_edit_page.homephone)
    assert contact_from_home_page.workphone == clear(contact_from_edit_page.workphone)
    assert contact_from_home_page.mobilephone == clear(contact_from_edit_page.mobilephone)
#    assert contact_from_home_page.faxphone == contact_from_edit_page.faxphone


def clear(s):
    return re.sub("[() -]", "", s)  # что заменять (скобки пробел минус) /на что заменять (на пустоту)
    # /где заменять(в строке)
