a = 17
b = 20

# if a>b:
#     print("a is greater than b")

# elif a==b:
#     print("a is equal to b")

# else:
#     print("a is smaller than b")


# if a>b:print("a is greater than b")  #short hand if


#print("greater") if a>b else print("smaller")   #short hand if else

#print("A") if a>b else print("=") if a==b else print("=")


# And 

a = 230
b = 87
c = 430

if a>b and c>a:
    print("Both cond are true",a)

a = 2
b = 4
c = 5

# or 

if a<b or b<a:
    print("At least one of the cond is true")


# nested if 

a = 40

if a > 10:
    print("a above 10")

    if a > 30:
        print("also above 30")

    else:
        print("but not above 30")
