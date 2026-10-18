import pickle

data={"name":"wassim","age":38,"Is_studednt":False}


with open("data.pkl","wb") as file:
    pickle.dump(data,file)

with open ("data.pkl","rb") as file:
    load=pickle.load(file)

print(load)





