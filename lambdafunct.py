# a = lambda n:n*n
# print(a(2))
# print(a(3))
# print(a(4))


# s =  lambda a,b,c:a+b*c
# print("The statement of {} {} and {} is {}".format(5,6,4,s(5,6,4)))


def is_odd(x):
    if x%2!=0:
        return True
    else: 
        return False
ele = [3,8,7,6,13,56]
l = list(filter(is_odd,ele))
print(l)



ele = [3,8,7,6,13,56]
a = list(filter(lambda x : x%2==0, ele))
print(a)