
def isPrimitive(lst):
    for g in range(3):
        for i in range(2, lst[g] + 1):
            if lst[0] % i == 0 and lst[1] % i == 0 and lst[2] % i == 0:
                return False
    return True
​
​
​
def is_prim_pyth_triple(lst):
    s = 0
    if isPrimitive(lst):
        for i in lst:
            if i != max(lst):
                s += i ** 2
    if s == max(lst) ** 2:
        return True
    else:
        return False

