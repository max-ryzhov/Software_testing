import pymysql.cursors
from fixture.orm import ORMFixture
from model.group_construct import Group
from model.contact_construct import Contact


db = ORMFixture(host='localhost', name='addressbook', user='root', password='')

try:
    lst = db.get_contacts_not_in_group(Group(group_id='327'))
    for item in lst:
        print(item)
    print(len(lst))
finally:
    pass    # db.destroy() - сессии автоматически закрываются ORM
