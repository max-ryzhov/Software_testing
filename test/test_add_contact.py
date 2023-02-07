# -*- coding: utf-8 -*-
from model.contact_construct import Contact
import pytest
import random
import string


# генератор случайных строк
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    random_str = "".join([random.choice(symbols) for symbol in range(random.randrange(maxlen))])
    return prefix + random_str


# генератор тестовых данных
test_data_contact = [Contact(firstname=random_string('firstname_', 7),
                             lastname=random_string('lastname_', 7),
                             nickname=random_string('nickname_', 7),
                             address=random_string('address_', 7),
                             company=random_string('company_', 7),
                             email=random_string('email_', 7),
                             email2=random_string('email2_', 7),
                             email3=random_string('email3_', 7),
                             mobilephone=random_string('mobilephone_', 7),
                             homephone=random_string('homephone_', 7),
                             secondphone=random_string('secondphone_', 7)) for i in range(1)]


@pytest.mark.parametrize('added_contact', test_data_contact, ids=[str(x) for x in test_data_contact])
def test_add_contact(app, added_contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(added_contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(added_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
