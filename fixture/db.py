import pymysql.cursors
from model.group_construct import Group
from model.contact_construct import Contact


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        # autocommit - отключает встроенное кэширование базы данных
        self.connection = pymysql.connect(host=host, user=user, password=password, database=name, autocommit=True)

    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select group_id, group_name, group_header, group_footer from group_list')
#            for row in cursor.fetchall():  # cursor.fetchall вывести данные в виде списка
            for row in cursor.fetchall():
                (id, name, header, footer) = row
                group_list.append(Group(group_id=str(id), group_name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return group_list

    def get_contact_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select id, firstname, lastname from addressbook where deprecated="0000-00-00 00:00:00"')
            #            for row in cursor.fetchall():  # cursor.fetchall вывести данные в виде списка
            for row in cursor.fetchall():
                (id, firstname, lastname) = row
                contact_list.append(Contact(cont_id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return contact_list

    def destroy(self):
        self.connection.close()
