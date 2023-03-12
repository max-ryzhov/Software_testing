import pymysql.cursors
from fixture.db import DbFixture

# PyMySQL - драйвер для СУБД MySQL


# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='addressbook',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    cursor = connection.cursor()    # cursor - указатель на данные в базе.
    cursor.execute('select * from group_list where group_id=410')    # cursor.execute извлечь данные
    for row in cursor.fetchall():    # cursor.fetchall вывести данные в виде строки
        print(row)
finally:
    connection.close()





# with connection:
#     with connection.cursor() as cursor:
#
#         # Create a new record
#         sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
#         cursor.execute(sql, ('webmaster@python.org', 'very-secret'))