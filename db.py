from pony.orm import *
from werkzeug import security
import werkzeug

db = Database()

db.bind(provider="sqlite", filename="main.sqlite", create_db=True)

class User(db.Entity):
    username=Required(str, unique=True)
    password=Required(str)
    age=Optional(int)

db.generate_mapping(create_tables=True)

@db_session
def create_user(uname, pwd, ag):
    if check_user_exixts(uname):
        print("user not created")
    else:
        n_pass = security.generate_password_hash(pwd, method='pbkdf2:sha256:500_000', salt_length=16)#pbkdf2:method:iterations where iterations is optional
        User(username=uname, password=n_pass, age=ag)

        print("user created")
    return "ok"

@db_session
def check_user_exixts(username):
    return select(u for u in User if u.username == username).exists()


 #without this tables are not created...