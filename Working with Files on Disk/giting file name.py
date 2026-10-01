import os
file_path="/path/to/student.txt"

file_name=os.path.basename(file_path)

print(f"File name : {file_name}")


file_path2="/path/to/prices.txt"

file_dir=os.path.dirname(file_path2)

print(f"Directory: {file_dir}")