from pony.orm import *
from datetime import datetime
from model.group_construct import Group
from model.contact_construct import Contact
# from pymysql.converters import decoders    # !!!!! преобзазователь типов данных для pony.orm


"""ПОНИ БУДЕТ ПЕРЕВОДИТЬ СОРЗДАННЫЙ НАМИ ORM-ЯЗЫК НА ЯЗЫК SQL-ЗАПРОСОВ"""
class ORMFixture:
    db = Database()    # объект - БД с которой работаем.

    """ОПИСЫВАЕМ ORM-МОДЕЛЬ В ВИДЕ КЛАССОВ (класс по сути - описывает отдельную таблицу)"""
    # внутри класса описываем набор свойств, привязанных к полям таблицы
    class ORMGroup(db.Entity):  # db.Entity - базовый класс, вложенный в объект db.
        # Так осуществляется привязка класса ORMGroup к db = Database()
        _table_ = 'group_list'  # название таблицы
        group_id = PrimaryKey(int, column='group_id')    # PrimaryKey - приоритетное поле идентификации объекта
        group_name = Optional(str, column='group_name')    # column = "название столбца в таблице"
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        # связь контактов и групп по столбцу id таблицы address_in_groups
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups", column='id', reverse='groups', lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(str, column='deprecated')    # !!! заменил тип на str, под pymysql.converters decoders
#        deprecated = Optional(datetime, column='deprecated')
        # связь групп и контактов по столбцу id таблицы address_in_groups
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column='group_id', reverse='contacts', lazy=True)

    """ПРИВЯЗЫВАЕМСЯ К КОНКРЕТНОЙ БД"""
    def __init__(self, host, name, user, password):
        # bind - метод привязки объектов к БД
        self.db.bind('mysql', host=host, database=name, user=user, password=password)    # , conv=decoders)
        self.db.generate_mapping()  # mapping сопоставляет свойства описанных КЛАССОВ с таблицами БД
        sql_debug(True)

    """ФУНКЦИИ ПРЕОБРАЗУЮЩИЕ ОБЪЕКТЫ ORMGroup в ОБЪЕКТЫ Group"""
    def convert_groups_to_model(self, groups):
        def convert(group):
            # attr.Group = attr.ORMGroup
            return Group(group_id=str(group.group_id), group_name=group.group_name, header=group.header,
                         footer=group.footer)
        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            # cont_id - свойство класса Contact. contact.id - свойство класса ORMContact
            return Contact(cont_id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname)
        return list(map(convert, contacts))    # возвращает список

    """ФУНКЦИИ, ПОЛУЧАЮЩИЕ СПИСКИ ОБЪЕКТОВ ИЗ БД"""
    @db_session  # помечаем что открывается сессия
    def get_group_list(self):
        # делаем выборку из таблицы, но не на языке sql, а на созданном нами языке ORMFixture.ORMGroup
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session  # помечаем что открывается сессия
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))
    # даты  deprecated преобразовываем в None

    @db_session  # помечаем что открывается сессия
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.group_id == group.group_id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)
