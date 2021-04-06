
def cap_space(txt):
​
    newtxt=""
    for i in txt:
        if i==i.upper():
             newtxt+=" "
        newtxt += i
    return newtxt.lower()
​
print(cap_space("helloWorld"))

