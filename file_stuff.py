import os
import shutil
import sys

print(os.getcwd())                      #Where are we?
print(os.listdir())                     #list files

#make and move
try:
    os.mkdir("directory_test1")
except FileExistsError:
    print("directory alread exists!")
base_file = "directory_test1"
dest_file = "directory_test3\\directory_test1"

try:
    shutil.move(base_file, dest_file)
except:
    print(sys.exc_info())

'''
try: #remove directory tree
    shutil.rmtree("directory_test2")
except:
    print(sys.exc_info())
'''
'''
try:
    os.rename("directory_test1", "directory_test2")
except:
    print(sys.exc_info())
'''
'''
try:                                    #copy a file
    from_dir = "directory_test1"
    to_dir = "directory_test3"
    shutil.copytree(from_dir, to_dir)

except:
    print(sys.exc_info())
'''

'''
#make dir
try:
    os.mkdir("directory_test1")

except FileExistsError:
    print("\n Directory already exists.")
'''