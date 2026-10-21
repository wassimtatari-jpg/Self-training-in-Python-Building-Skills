import pickle

class UserFile:
    def __init__(self,filepath):
        self.filepath=filepath
        self.file=open(filepath,"r")
        self.data=self.file.read()
    def __getstate__(self):
        state=self.__dict__.copy()
        del state["file"]
        return state
    def __setstate__(self,state):
        self.__dict__.update(state)
        self.file=open(self.filepath,"r")
file_path="student.txt"

with open(file_path,"w") as f:
    f.write("Data writed")

obj=UserFile(file_path)

my_file=pickle.dumps(obj)

print(my_file)

my_load=pickle.loads(my_file)

print(my_load)
print(my_load.data)
print(my_load.file.closed)
obj.file.close()
my_load.file.close()
