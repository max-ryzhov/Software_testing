# -*- coding: utf-8 -*-
import random
from model.contact_construct import Contact


def test_update_contact(app, db):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Default", lastname="User", address="for_modification"))

    mod_contact = Contact(firstname="mod_name", lastname="mod_lastname", address="mod_address", mobilephone="+0000",
                          email="mod@gmail.com", title_user='Good')
    # загрузил начальный список из БД
    old_contacts = db.get_contact_list()
    # выбрал рандомный контакт для модификации
    contact = random.choice(old_contacts)
    # сохранил id и индекс выбранного контакта
    mod_contact_id = contact.cont_id
    mod_contact_index = old_contacts.index(contact)
    # модифицировал контакт в браузере по id
    app.contact.modify_contact_by_id(mod_contact_id, mod_contact)
    # вернул модифицированному контакту id-шник
    mod_contact.cont_id = mod_contact_id
    # загрузил обновленный список из БД
    mod_contacts = db.get_contact_list()
    old_contacts[mod_contact_index] = mod_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(mod_contacts, key=Contact.id_or_max)
