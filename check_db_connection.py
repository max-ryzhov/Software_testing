import pymysql.cursors
from fixture.orm import ORMFixture


db = ORMFixture(host='localhost', name='addressbook', user='root', password='')

try:
    lst = db.get_contact_list()
    for item in lst:
        print(item)
    print(len(lst))
finally:
    pass    # db.destroy() - сессии автоматически закрываются ORM
