def sum(*n):
    result = 0
    for x in n:
        result = result + x
    print("The sum is",result)

sum(1)
sum(10,20)
sum(10,70,20)
   



def sum(name,*n):
    result = 0
    for x in n:
        result = result + x
    print("The sum is",":",name,result)

sum("pranali",1)
sum("abc",10,20)
sum("xyz",10,70,20)
   

def sum(*n,name):
    result = 0
    for x in n:
        result = result + x
    print("The sum is",":",name,result)

sum(1,name="pranali")
sum(10,20,name="abc") 
sum(10,70,20,name="xyz")