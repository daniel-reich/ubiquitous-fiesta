
def max_product(lst):
    lst = sorted(lst)
    (a1,a2,a3),(b1,b2,b3) = lst[-3:], lst[:2] + lst[-1:]
    return max(a1*a2*a3, b1*b2*b3)
    
def min_product(lst):
    return -max_product(-x for x in lst)

