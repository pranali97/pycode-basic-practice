f1 = open("guido.jpg","rb")
f2 = open("newpic.jpg","wb")
bytes = f1.read()
f2.write(bytes)
print("New image is available with the name: newpic.jpg")