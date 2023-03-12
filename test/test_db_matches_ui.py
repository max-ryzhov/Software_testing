from model.group_construct import Group
from timeit import timeit


def test_group_list(app, db):
#    ui_list = app.group.get_group_list()    # формируем список групп со свойствами из ui
    print(timeit(lambda: app.group.get_group_list(), number=1))

    def clean(group):    # функция, отбрасывает header и footer, и удаляет пробелы спереди и сзади имени
        return Group(group_id=group.group_id, group_name=group.group_name.strip())

#    db_list = map(clean, db.get_group_list())    # формируем список групп из db, прменяя к каждой группе def clean
    print(timeit(lambda: map(clean, db.get_group_list()), number=1000))    # формируем список групп из db,
# прменяя к каждой группе def clean

    assert False    # sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
