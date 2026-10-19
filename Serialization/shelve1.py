import shelve

data = {'name': 'Eve', 'age': 28, 'is_student': False}


with shelve.open("data.shelve") as db:
    db["person"]=data

with shelve.open("data.shelve") as db:
    my_load=db['person']
print(my_load)


