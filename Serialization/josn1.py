import json

data={"name":"wassim","age":38,"Is_studednt":False}

#convert to string
josn_string=json.dumps(data)
print(josn_string)

# Serialize object to JSON file
with open("data.json","w") as file:
    json.dump(data,file)

# Deserialize object from JSON string
my_load=json.loads(josn_string)
print(my_load)



# Deserialize object from JSON file

with open("data.json","r") as file:
    load=json.load(file)
print(load)




