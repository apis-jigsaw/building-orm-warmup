class User:
    # class attribute
    __table__ = 'users'
    # class attribute
    columns = ['name', 'birthday']
    
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday