import yaml

data = {'name': 'Carol', 'age': 27, 'is_student': False}

string_yaml=yaml.dump(data)

print(string_yaml)

with open("data.yaml","w") as file:
    yaml.dump(data,file)

my_load=yaml.load(string_yaml,Loader=yaml.FullLoader)
print(my_load)


with open("data.yaml","r") as file:
    load=yaml.load(file,Loader=yaml.FullLoader)
print(load)



