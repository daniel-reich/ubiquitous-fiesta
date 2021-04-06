
def is_legitimate(lst):
    return not(any(lst[0])or any(lst[-1])) and all(i[0]==0 and i[-1]==0 for i in lst)

