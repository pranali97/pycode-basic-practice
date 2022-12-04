# a = "jdjdhajkdnasndamnxk"
# print(a.find("a"))

# any = input("enter anything: ")
# l = []
# for i in any:
#     if i not in l:
#         l.append(i)
# output = "".join(l)
# # print(output)

# d = {100: "salim", 200: "sham"}
# d[300] = "shiva"
# print(d.keys())

# for k,v in d.items():
#     print("{}={}".format(k,v))


d = input("enter something: ")
x = {}
for i in d:
    if i not in x.keys():
        x[i]=1
    else:
        x[i]= x[i]+1
for k,v in x.items():
    print("{} occurs {} times".format(k,v))