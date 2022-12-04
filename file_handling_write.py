
with open("abc.txt","w") as f:
    f.write("hello\n")
    f.write("ho")
    print("is file close?",f.closed)
print("is file close?",f.closed)

data = "same\n"
with open("txtfile.txt","r+") as f:
    text = f.read()

data1 = "add some\n"
with open("txtfile.txt","a+") as f:
    text = f.write(data1)


    # print(text)
    
    
    # f.write(data)

somedata = "hello how are you"
f = open("sometext.txt","w")
f.write(somedata)

with open('sometext.txt','r+') as f: #r+ read and then write
    text = f.read()
    print(text)
    # print(f.tell())  to tell where is the current position of cursor 
    f.seek(6)
    print(f.tell())
    f.write("is")
    f.seek(8) 
    f.write(" going on!")
    f.seek(0)
    some = f.read()
    print(some)


with open ("qwerty.txt","w") as f:
    f.write("hello\n")
    # text = f.read() 
    f.write("hey")
    # text = f.read()
    # print(text)

with open("random.txt", "r+") as f:
    f.write("All is well ")
    f.write("keep the hardworking")
    f.write("make sense")

    print("The current position of the cursor is",f.tell())
    f.seek(12)
    print("The current position of the cursor is",f.tell())
    f.write("somthing")
    f.seek(0)
    text = f.read()
    print("Data after modification",text)