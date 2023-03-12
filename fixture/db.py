import pymysql.cursors
from model.group_construct import Group


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        # autocommit - отключает встроенное кэширование базы данных
        self.connection = pymysql.connect(host=host, user=user, password=password, database=name, autocommit=True)

    def get_group_list(self):
        lst = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('select group_id, group_name, group_header, group_footer from group_list')
#            for row in cursor.fetchall():  # cursor.fetchall вывести данные в виде списка
            for row in cursor.fetchall():
                (id, name, header, footer) = row
                lst.append(Group(group_id=str(id), group_name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return lst

    def destroy(self):
        self.connection.close()
