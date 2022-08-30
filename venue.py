class Venue:
    __table__ = 'venues'
    columns = ['name']
    def __init__(self, name):
        self.name = name