# f = open("demo.txt","r")
# # print(f.readline())
# print(f.readline())
# f.close()

# for x in f:
#     print(x)

# with open("demopass.txt","r") as f:
#     f.read("the file has more content")
#     f.close()
    
# f = open("demopass.txt", "r")
# print(f.read())

import os
if os.path.exists("qwerty.txt"):
    os.remove("qwerty.txt")
else:
    print("file does not exist")