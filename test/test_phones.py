import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(0)
    assert contact_from_home_page.homephone == clear(contact_from_edit_page.homephone)
    assert contact_from_home_page.workphone == clear(contact_from_edit_page.workphone)
    assert contact_from_home_page.mobilephone == clear(contact_from_edit_page.mobilephone)
    #assert contact_from_home_page.secondphone == clear(contact_from_edit_page.secondphone)


def test_phones_on_contact_view(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    #assert contact_from_view_page.secondphone == contact_from_edit_page.secondphone
    print()
    print(f'{contact_from_view_page.homephone} = {contact_from_edit_page.homephone}')
    print(f'{contact_from_view_page.workphone} = {contact_from_edit_page.workphone}')
    print(f'{contact_from_view_page.mobilephone} = {contact_from_edit_page.mobilephone}')


def clear(s):
    return re.sub("[() -]", "", s)  # что заменять (скобки пробел минус) /на что заменять (на пустоту)
    # /где заменять(в строке)
