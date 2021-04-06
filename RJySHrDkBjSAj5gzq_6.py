
def perm(n):
    tot = 1
    while n > 1:
        tot *= n
        n -= 1
    return tot
​
​
def nespers(lst: list) -> int:
    if all(True if type(i) == int else False for i in lst):
        return perm(len(lst))
    else:
        tot = perm(len(lst))
        for i in lst:
            if type(i) == list:
                tot *= nespers(i)
    return tot

