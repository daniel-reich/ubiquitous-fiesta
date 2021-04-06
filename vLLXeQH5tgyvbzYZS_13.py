
def co_prime(num1, num2):
    lst = [num1, num2]
    lst.sort()
    div = lst[0]
    cent = lst[1]
    while div != 1:
        temp = div
        div = cent % div
        cent = temp
        if div == 0:
            return False
    return True
​
​
def is_prim_pyth_triple(lst):
    lst.sort()
    if lst[0] ** 2 + lst[1] ** 2 != lst[2] ** 2:
        return False
    for i in range(-1, 2):
        if not co_prime(lst[i], lst[i+1]):
            return False
    return True

