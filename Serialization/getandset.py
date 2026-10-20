import pickle

class CustomClass:
    def __init__(self,value):
        self.value=value
        self.internal_value="Internal value"
    def __getstate__(self):
        state=self.__dict__.copy()
        del state["internal_value"]
        return state
    def __setstate__(self,state):
        self.__dict__.update(state)
        self.internal_value="Restor"
        
obj=CustomClass(45)

print("Orjinal object",obj)


string_obj=pickle.dumps(obj)

print("Serilitation",string_obj)

des_obj=pickle.loads(string_obj)
print("Desrilitaion",des_obj)



       
