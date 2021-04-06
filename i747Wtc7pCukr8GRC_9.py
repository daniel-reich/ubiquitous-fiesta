
def max_product(lst):
    lst.sort()
    a = lst[0] * lst[1] * lst[-1]
    b = lst[-1] * lst[-2] * lst[-3]
    return max(a,b)
​
def min_product(lst):
    lst.sort()
    a = lst[0] * lst[1] * lst[2]
    b = lst[-1] * lst[-2] * lst[0]
    return min(a,b)

