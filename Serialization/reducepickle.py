import pickle

class Customclass:
    def __init__(self,value):
        self.value=value
    def __reduce__(self):
        return(self.__class__,(self.value,))
    def __repr__(self):
        return f"Custom class(value={self.value})"

my_obj=Customclass(55)

serialization_ob=pickle.dumps(my_obj)
print("serialization object:",serialization_ob)

deserialization_ob=pickle.loads(serialization_ob)
print("Deserilaization object:",deserialization_ob)