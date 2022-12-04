# filter


def is_odd(x):
    if x%2!=0:
        return True
    else: 
        return False
ele = [2,4,6,8]
l = list(filter(is_odd,ele))
print(l)



ele = [3,8,7,6,13,56]
a = list(filter(lambda x : x%2==0, ele))
print(a)

# Map 
def double(n):
    return 2*n

elem = [3,4,5,6,7]
# x = type(map(double,elem)) 
x = list(map(double,elem))
print(x)

# lambda map

num = [2,3,4,5,10,6]
x = list(map(lambda x:2*x,num))

ele1 = [20,30,40,50]
ele2 = [2,3]
mapped = list(map(lambda x,y:x+y,ele1,ele2))
print(mapped)
 
# reduce 
from functools import *
from operator import add

l = [10,20,30,40,50,60]
result = reduce(lambda x,y:x+y,l)
print(result)

print(reduce(add,[10,20,30]))