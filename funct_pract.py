s = lambda n:n*n
print("The square of {} is {}".format(4,s(4)))
print("The square of {} is {}".format(5,s(5)))

def wish(name):
    print("good morning",name)

greeting = wish
print(id(greeting))
print(id(wish))
wish("Pranali")
wish("Anurag")


def wish(name):
    print("good morning",name)

greeting = wish
greet =  greeting
# wish("hi")
greeting("hello")
greet("good")
wish("good")

