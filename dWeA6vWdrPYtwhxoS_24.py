
def count_number(lst, c=0):
    if not lst:
        return c
    
    if type(lst[0])!=list:
        if type(lst[0])!=str:
            c+=1
        return count_number(lst[1:], c)
    
    return count_number(lst[0]+lst[1:], c)

