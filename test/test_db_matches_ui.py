from model.group_construct import Group


def test_group_list(app, db):
    ui_list = app.group.get_group_list()    # формируем список групп со свойствами из ui

    def clean(group):    # функция, отбрасывает header и footer, и удаляет пробелы спереди и сзади имени
        return Group(group_id=group.group_id, group_name=group.group_name.strip())

    db_list = map(clean, db.get_group_list())    # формируем список групп из db, прменяя к каждой группе def clean
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
