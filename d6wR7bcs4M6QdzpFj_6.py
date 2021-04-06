
def repeat(lst, n):
    lst *= n
    return lst
​
def add(lst, x):
    lst.append(x)
    return lst
​
def remove(lst, i, j):
    l = [lst[k] for k in range(len(lst)) if k < i or k > j]
    lst.clear()
    lst += l
    return lst
​
def concat(lst, lst2):
    lst += lst2
    return lst

