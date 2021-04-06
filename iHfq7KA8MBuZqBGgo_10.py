
def is_legitimate(lst):
    for i in lst[0]:
        if i==1:
            return False
    for i in lst[-1]:
        if i==1:
            return False
    for i in lst:
        if i[0]==1 or i[-1]==1:
            return False
    return True

