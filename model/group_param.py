from sys import maxsize


class GroupParam:
    def __init__(self, group_name=None, header=None, footer=None, group_id=None):
        self.group_name = group_name
        self.header = header
        self.footer = footer
        self.group_id = group_id

    def __repr__(self):
        return f'{self.group_id}:{self.group_name}'

    def __eq__(self, other):
        return (self.group_id == other.group_id or self.group_id is None or other.group_id is None) \
               and self.group_name == other.group_name

    def id_or_max(self):
        if self.group_id:    # обращаемся к группе из списка и проверяем, что group_id - true сущность
            return int(self.group_id)    # возвращаем group_id, переведенное в число
        else:    # None - не true сущность
            return maxsize
