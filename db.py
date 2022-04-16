from pony.orm import *

db = Database()

db.bind(provider="sqlite", filename="main.db", create_db=True)

class User(db.Entity):
    username:str
    password:str
    age:int|None
    #TODO:add posts maybe "required" instead of "|"

db.generate_mapping(create_tables=True) #without this tables are not created...

@db_session
def create_user():
    #create user logic
    return "ok"

@db_session
def check_user_exixts():
    #this will be sed A LOT
    return True
