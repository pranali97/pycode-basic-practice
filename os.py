import os,sys

fname = input("Enter a file name: ")

if os.path.isfile(fname):
    print("file exists",fname)
    f = open(fname,"r")
    print("the content of file:")
    data = f.read()
    print(data)
    f.close()
else:
    print("file doesn't exist",fname)
    # sys.exit(0)


