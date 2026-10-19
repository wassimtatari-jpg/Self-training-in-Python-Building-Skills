import pickle

employ_data={"Name":"Mohamed","Age":38,"position":"python Developer","skills":["OOP","Python","Data Analysis"]}

with open("employ_data.pkl","wb") as file:
    pickle.dump(employ_data,file)

with open("employ_data.pkl","rb") as file:
    load=pickle.load(file)

print(load)