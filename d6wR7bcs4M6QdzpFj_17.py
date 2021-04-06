
def repeat(lst, n):
    L = len(lst)
    for y in range(n - 1):
        for idx in range(L):
            lst.append(lst[idx])
    return lst
​
def add(lst, x):
    lst.append(x)
    return lst
​
def remove(lst, i, j):
    L = len(lst)
    for y in range (j + i - 1):
        lst.pop(i)
    return lst
​
def concat(lst, lst2):
    lst.extend(lst2)
    return lst

