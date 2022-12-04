def outer_function():
    print("Outer function started")

    def inner_function():
        print("inner function executed")
    inner_function()

outer_function()


def f1():
    def inner_function(a,b):
        print("the sum is: ",a+b)
        print("the average is: ",(a+b/2))
        print("the average is: ",a+b/2)
    inner_function(3,5)
    inner_function(9,5)
    inner_function(11,22)
    inner_function(30,15)


f1()