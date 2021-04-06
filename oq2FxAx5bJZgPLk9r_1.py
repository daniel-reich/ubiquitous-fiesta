
def sock_merchant(lst):
    return sum(lst.count(i)//2 for i in set(lst))

