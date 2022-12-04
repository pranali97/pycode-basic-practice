def cal(a,b):
    sum = a+b
    mul = a*b
    sub = a-b
    div = a//b
    return sum, mul, sub, div

q = cal(100,20)
for i in q:
    print(i)
print(type(q))
