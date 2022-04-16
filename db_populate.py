from db import *

dummy_data=[
    {
        "name":"MCA",
        "password":"MCA",
        "age":43
    },{
        "name":"Mike-D",
        "password":"Mike-D",
        "age":44
    },{
        "name":"AD-Rock",
        "password":"AD-Rock",
        "age":45
    }, {#this needs to be removed from time to time
        "name":"Saxsquatch",
        "password":"Saxsquatch",
        "age":216
    }
]
"""
for user in dummy_data:
    create_user(user["name"], user["password"], user["age"])
for user in dummy_data:
    check_user_exixts(user["name"])
"""
