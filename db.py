from pony.orm import *

db = Database()

db.bind(provider="sqlite", filename="main.sqlite", create_db=True)

class User(db.Entity):
    username=Required(str, unique=True)
    password=Required(str)
    age=Optional(int)

db.generate_mapping(create_tables=True)

@db_session
def create_user(uname, pwd, ag):
    User(username=uname, password=pwd, age=ag)

    return "ok"

@db_session
def check_user_exixts(username):
    query = select(u for u in User if u.username == username)
    return bool(query.count())


 #without this tables are not created...