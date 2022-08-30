class User:
    columns = ['name', 'birthday']
    __table__ = 'users'
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday