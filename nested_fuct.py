def outer():
    print("outer function executed")
    def inner():
        print("inner function executed")
    print("outer function execution started")
    return inner()

f = outer()
print(id(f))
print(type(f))
# f()
# f()