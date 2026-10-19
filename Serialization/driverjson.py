import json

driver={"name":"mohamed","age":39,"city":"Tangier","skils":["Transportation","Trips with discrebtion","Visit good place"]}

my_file=json.dumps(driver)
print(my_file)

with open("driver.json","w")as file:
    json.dump(driver,file)

my_file_load=json.loads(my_file)
print(my_file_load)


with open("driver.json","r")as file:
    load=json.load(file)
print(load)