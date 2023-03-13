from pony.orm import *
from datetime import datetime
from model.group_construct import Group
from model.contact_construct import Contact


# ПОНИ БУДЕТ ПЕРЕВОДИТЬ НА ЯЗЫК SQL-запросов
class ORMFixture:
    db = Database()

    # ОПИСЫВАЕМ СТРУКТУРУ
    # внутри класса описываем набор свойств, привязанных к таблице
    class ORMGroup(db.Entity):  # db.Entity привязали класс к БД. этот класс описывает объекты, кот. сохраняются в БД
        _table_ = 'group_list'  # название таблицы
        group_id = PrimaryKey(int, column='group_id')  # column = "название столбца в таблице"
        group_name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')

    # ПРИВЯЗЫВАЕМ СВОЙСТВА К СТОЛБЦАМ БД
    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()  # mapping как раз сопоставляет свойства описанных классов с полями таблиц
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(group_id=str(group.group_id), group_name=group.group_name, header=group.header,
                         footer=group.footer)

        return list(map(convert, groups))

    # ФУНКЦИИ, ПОЛУЧАЮЩИЕ СПИСКИ ОБЪЕКТОВ
    @db_session  # помечаем что открывается сессия
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

