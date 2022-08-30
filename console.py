from user import User
from venue import Venue
import psycopg2
conn = psycopg2.connect(dbname = 'crm_db')
cursor = conn.cursor()

sam = User('sam', '8/30/1999')
bob = User('bob', '8/30/1999')
chipotle = Venue('Chipotle')

# remove the hard coding of items 
# particular to user so that we can also save venue using the save method
def save(obj):
    breakpoint()
    insert_str = f"""INSERT INTO {obj.__table__} (name, birthday) VALUES (%s, %s);"""
    # cursor.execute(insert_str, ('bob', '8/3/1997'))
    # conn.commit()
    return insert_str


# save(sam)
# save(chipotle)


