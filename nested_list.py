l = [[10,20,30],[40,50,60],[70,80,90]]
print(l)
# for x in range(l):
print("Elements row wise")
for x in l:
    print(x)
print("Elements in matrix form")
for i in range(len(l)):
    # print(i)
    for j in range(len(l[i])):
        print(l[i][j],end=' ')
    print()


# list comprehension 
# [expression for loop condition]

l2 = [x for x in range(1,21)]
l3 = [ x for x in l2 if x%2==0]
print(l2)
print("l3",l3)
print(type(l3)) 

l5 = [2**x for x in range(1,21) if x%2!=0]
print("l5",l5)

l6 = [x for x in range(1,21) if (2**x)%2!=0]
print("l6",l6)


words = ['mango','apple','orange','banana']
l = [w for w in words if len(w)>=6]
print(l)  

n1 = [11,22,33,44,55]
n2 = [66,22,11,100,200]

n3 = [x for x in n1 if x not in n2]
print(n3)


words = "Keep smiling, because life is a beautiful thing and there is so much to smile about".split(" ")
print(words)

l1 = [w.lower() for w in words ]
l2 = [w.upper() for w in words ]
l3 = [[w.upper(),len(w)] for w in words ]
print(l1)
print(l2)
print(l3)
s = [1,2,3,4,5,6,7,8,9]
slice =s[-5:-1:-1]
slice1 = s[-2:-3:-1]
print(slice1)

t = '98765'
s = t[-2:-5:-1]
print(s)


vowels = ['a','e','i','o','u','A','E','I','O']
search = (input("Enter the word::  "))
found = []
for letter in search:
    # print(letter)
    if letter in vowels:
        if letter not in found:
            found.append(letter)
print(found)
print("Number of different vowels present in",search,"and length is",len(found))

vowels = ['a','e','i','o','u']
search = (input("Enter the word::  "))
found = []
for letter in search:
    # print(letter)
    if letter.lower() in vowels:
        if letter.lower() not in found:
            found.append(letter.lower())
print(found)
print("Number of different vowels present in",search,"and length is",len(found))