
def josephus(n):
    lst = [i for i in range(n)]
    if(len(lst) < 1):return False
​
    pos = 1
    while len(lst) > 1:
        lst.pop(pos)
        pos = (pos + 1) % len(lst)
    return lst[0]

