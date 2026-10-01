import os

file_path="car.txt"

file_name=os.path.splitext(os.path.basename(file_path))[0]

print(file_name)