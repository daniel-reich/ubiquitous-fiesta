
def sum_list(lst, l=0):
    for i in lst:
        if type(i)==list:
            l += (sum_list(i))
        elif type(i)==int:
            l += i
    return l

