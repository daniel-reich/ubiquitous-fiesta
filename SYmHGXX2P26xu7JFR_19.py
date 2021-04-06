
def number_groups(group1, group2, group3):
    a, b, c = set(group1), set(group2), set(group3)
​
    lst = []
​
    for i in a:
        if (i in b) or (i in c):
            if not(i in lst):
                lst.append(i)
​
    for j in b:
        if (j in a) or (j in c):
            if not(j in lst):
                lst.append(j)
​
    for x in c:
        if (x in a) or (x in b):
            if not(x in lst):
                lst.append(x)
​
    lst.sort()
    
    return lst

