
def asc_des_none(lst, s):
    if s=='Asc':
        lst.sort()
        a=lst
    elif s=='Des':
        lst.sort()
        lst.reverse()
        a=lst
    elif s=='None':
        a=lst    
    return a

