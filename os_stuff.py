import os

#os name
print(os.name)

#cwd - current working directory
print(os.getcwd())
i=0
list_files = os.listdir()
for f in list_files:
    i=i+1
    print(str(i)+ ". " + f)
'''
for dirpath, dirname, files in os.walk("."):
    print(f"Found directory --> {dirpath}")
    for file_name in files:
        print("    " + file_name)
'''
'''
platform end line character
Windows = "\r \n"
Linux = "\n"
Mac = "\r"
'''
os.linesep

#run shell command, like ping
#print (os.system("ping 127.0.0.1"))
ipaddy= input("What is the IP you want to ping? ")
print (os.system("ping " + ipaddy))

