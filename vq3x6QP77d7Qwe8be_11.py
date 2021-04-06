
def odd_square_patch(lst):
    for i in range(1,len(lst)+2):
        if not has_patch(lst, i):
            return i - 1
​
​
def has_patch(lst, n):
    if n>len(lst) or n>len(lst[0]):
        return False
    for i in range(len(lst)-n+1):
        for j in range(len(lst[0])-n+1):
            if is_odd([[l for l in k[j:j+n]]for k in lst[i:i+n]]):
                return True
    return False
def is_odd(lst):
    for i in lst:
        for j in i:
            if j % 2 != 1:
                return False
    return True

