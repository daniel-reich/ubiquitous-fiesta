
def tuck_in(lst1, lst2):
​
    pos = 1
​
    for i in range(len(lst2)):
        lst1.insert(pos, lst2[i])
        pos += 1
​
    return lst1

