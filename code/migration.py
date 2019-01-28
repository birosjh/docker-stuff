from pony.orm import *

db = Database()
db.bind(provider='mysql', host='db', user='root', passwd='', db='sample')


class Person(db.Entity):
    name = Required(str)
    age = Required(int)

db.generate_mapping(create_tables=True)
