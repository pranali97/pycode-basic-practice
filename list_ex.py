# l = list(range(0,10))
# print(l)

# s = 'pranali'
# print(list(s))

# s = "help the nation"
# l = s.split()
# print(type(l))
# print(l)

# l = [10,20,30,40,50,60]
# l1 = [10,20,[30,40],50,50]

# print(l[::])
# print(l[::2])
# print(l[::-1])
# print(l[::-2])
# print(l1[0:3])

l = [1,2,3,4,5,6,7,8,2,10,2]
i = 0
while i < len(l):
    print(i)
    i=i+1
print("--------------------------------------")
for x in l:
    print(x)

print("even numbers: ")
for z in l:
    if z%2==0:
        print(z)
print("posit index and negat index")
l2 = ["A","B","C","D","E","F"]
x = len(l2)
print(x)
for i in range(x):
    # print(i)
    print(l2[i],"at positive index",i,"and at negative index",i-x)


# list function and method 

def myfunc():
    print("It is a function")

class students:
    def info(self):
        print("It is a method don't get confused")

myfunc()
s = students()
s.info()


# len()
# count()

b = [10,23,11,34,23,11,10,34,11,56,78,34]
c = b.count(11)
i = b.index(23)
print(c)
print(i)

# program 

# l3 = [11,22,33,44,55,66,77,88,99]
# ele = int(input("Enter the element to search: "))
# if ele in l3:
#     print(ele, "available and its first occurance is",l3.index(ele))
# else:
#     print(ele, "not available")


# program append

l = []
l.append("a")
l.append("b")
l.append("c")
l.append(1)
l.append(2)
l.append(3)
print(l)

l.insert(-20,99)
l.insert(4,777)

print(l)              
print(l.index(99))
print(l.index(777))
# print(l)

z1 = ["cat","dog","cow"]
z2 = ["tiger","lion","cheetah"]
z1.append(z2)
print(z1)

# x = []
# for i in range(0,110,10):
#     if i%10==0:
#         x.append(i)
# print(x)
    
# insert 

# ins =  [3,4,6,7]
# ins.insert(50,100)
# print(ins)

# # extend 
# a = ["black","red","blue"]
# b = ["yellow","orange","pink"]
# a.extend(b)
# c = a+b
# print(a)
# print(b)
# print(c)

# j = [1,2,3]
# k = [9,8,7]
# # j.extend("pranali")
# j.append("pranali")
# print(j)

# remove 
# j.remove(3)
# print(j)

# s = [23,45,67,12,26,39,40]
# search = int(input("enter element to be removed: "))

# if search in s:
#    s.remove(search)
#    print("Removed successfully")
#    print(s)
# else:
#     print("specified element is not availables") 

# pop 

list_num = [1,2,3,45,6]
print(list_num)
print(list_num.pop(4))
print(list_num)

# append, extend, insert  ----increase the length
# pop, remove  ---> decrease thelength 


# reverse()

lll = [2,3,4,5,6,7]
lll.reverse()
print(lll)

# sort() 

s = [34,67,45,12,90,13,45,21]
s1 = ["boy","cat","apple"]
s3 = ["Boy","Cat","Dog","apple"]
s4 = ["12","34","56","black","red"]  #sort type is used for homogeneous element only
s5 = [1,2,3,"a","b"]  #type error
s4.sort()
s1.sort()
s.sort(reverse=True)
s3.sort()
print(s1)
print(s)  
print(s3)
print(s4)

z = [3,2,1]
v = z
v.pop()
print(z)

# creation of duplicate by slicing 

a = [2,3,4]
b = a[:]
b[1]=8   #cloning object
print(a)

c = [3,4,5,6]
d = c.copy()  #copy
d[2] = 100
print(c)
print("d:",d)

# mathematical operator 

a = [2,3,4,5]
b = [4,5,6,7]

c = a+b 
d = a +[10]
e = b + ['s']
f = a*10 
print(c)
print(d)
print(e)
print(f)
import sys
print(len(sys.argv))
print(len(sys.argv[0]))
