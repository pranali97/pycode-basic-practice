import os, sys

fname = input("Enter a file name: ")
if os.path.isfile(fname):
    print("file exist",fname)
    f = open(fname,"r")
else:
    print("file doesn't exist", fname)
    sys.exit(0)

print("The content of file is: ")
data = f.read()
print(data)


file_name = input("Enter a file name: ")
if os.path.isfile("file_name"):
    print("file exist",file_name)
    f = open("file_name","r")
else:
    print("file doesn't exist", fname)
    sys.exit(0)




