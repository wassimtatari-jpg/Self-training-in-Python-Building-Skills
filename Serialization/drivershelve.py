import shelve

driver={"name":"mohamed","age":39,"city":"Tangier","skils":["Transportation","Trips with discrebtion","Visit good place"]}

with shelve.open("driver.shelve") as db:
    db["my driver"]=driver

with shelve.open("driver.shelve") as db:
    my_load=db["my driver"]

print(my_load)