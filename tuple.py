# a = "abcd"
# p,q,r,s= a
# print("x=",p,"y=",q,"z=",r,"o=",s)

# packing / unpacking
# a=10
# b=20
# c=30
# d=90

# t = {a,b,c,d}
# print(t)

# wap to take input from keboard as tuple and  print sum of number, average.

tup = eval(input("enter the values: "))
t = len(tup)
sum = 0 
for x in tup:
    sum =sum + x
print("sum:", sum)
# print("Average:", sum/t)