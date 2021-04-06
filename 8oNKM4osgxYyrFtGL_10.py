
string = "abcd"
astring = list(string)
​
def multiply(l):
    fulllist = []
    for x in l:
       fulllist.append(list([x]*len(l)))
    return fulllist
     
print(multiply(astring))

