from sys import maxsize


class Contact:
    def __init__(self, cont_id=None, firstname=None, lastname=None, middlename=None, nickname=None, title_user=None,
                 address=None, company=None, email=None, mobilephone=None, homephone=None, workphone=None,
                 secondphone=None):
        self.cont_id = cont_id
        self.firstname = firstname
        self.lastname = lastname
        self.middlename = middlename
        self.nickname = nickname
        self.title_user = title_user
        self.address = address
        self.company = company
        self.email = email
        self.mobilephone = mobilephone
        self.homephone = homephone
        self.workphone = workphone
        self.secondphone = secondphone

    def __repr__(self):
        return f'{self.cont_id}:{self.firstname}:{self.lastname}:{self.homephone}:{self.workphone}'

    # переопределяем сравнение. в кач. агрументов передаем self-объект и other-объект
    def __eq__(self, other):
        # сравниваем св-ва self-объекта и  other-объекта: cont_id, firstname и lastname
        return (self.cont_id == other.cont_id or self.cont_id is None or other.cont_id is None) \
               and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.cont_id:    # обращаемся к контакту из списка и проверяем, что cont_id - true сущность
            return int(self.cont_id)    # возвращаем cont_id, переведенное в число
        else:    # None - не true сущность
            return maxsize
