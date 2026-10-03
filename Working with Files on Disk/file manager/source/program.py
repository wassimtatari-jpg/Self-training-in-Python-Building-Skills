import os,shutil

user_source=input("Enter file path : ")

if os.path.exists(user_source):
    print(f"File {user_source} is exist")
else:
    print(f"File {user_source} is not exist")
if os.path.isfile(user_source):
    print(f"{user_source} is file")
    file_name=os.path.basename(user_source)
    print(f"File name : {file_name}")
    directory="moved"
    file_name1=input("enter file name to join :")
    full=os.path.join(directory,file_name1)
    print(full)
    user_file_delet=input("Enter name file to delete:")
    if user_file_delet==user_source:
        os.remove(user_file_delet)
    else:
        print("file not exist")
    user_file_moved = input("Enter the file name to move :")
    shutil.move(user_file_moved, full)

    if os.path.exists(full):
        print(f"File successfully moved to: {full}")
    else:
        print("File was not moved")

elif os.path.isdir(user_source):
    print(f"{user_source} is Directory")
    for file in os.listdir(user_source):
        print(file)
    for file in os.listdir(user_source):
        print(os.path.splitext(file))
    for file in os.listdir(user_source):
        filename,extention=os.path.splitext(file)
        print(f"File name: {filename}")
        print(f"Extention : {extention}")
else:
    print(f"{user_source} is nither a file nor Directory")
