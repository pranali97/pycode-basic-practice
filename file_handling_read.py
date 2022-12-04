# read() To read total data from file 

with open("random.txt","r") as file:
    data = file.read()
    # print(data)

# file = open("random.txt","r")
# data = file.read()
# print(type(data))
# file.close()



# read(n) To read n characters from file
with open("random.txt","r") as file:
    data = file.read(10)
    # print(data)
    file.close()



# readline() read only 1 line
# with open("random.txt","r") as f:
    # print(f.readline(),end = " ")
    # print(f.readline(),end = " ")
    # print(f.readline(),end= " ")



# readlines  to read all lines into a list 
with open("random.txt", "r") as f:
    list = f.readlines()
    for i in list:
        print(i,end="")

 