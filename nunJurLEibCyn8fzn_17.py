
def filter_list(lst):
    a = 1
    mylist=[]
    print(len(lst))
    for i in range(len(lst)):
        if type(lst[i]) is type(a):
            mylist.append(lst[i])
    return mylist
​
result = filter_list(['g',3,2])
print(result)

