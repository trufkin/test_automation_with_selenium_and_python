import os
current_directory = os.path.dirname(__file__) # os.path.abspath(__file__)
current_dir = os.path.abspath(os.path.dirname(__file__))
current_file=os.path.join(current_directory,'file.txt')

print(current_directory)
print(current_dir)
print(current_file)