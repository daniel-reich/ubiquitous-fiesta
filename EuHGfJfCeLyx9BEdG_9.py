
#recursion
​
def party_people(lst):
    a = sorted(lst)
    if len(a)>0:
        if a[-1] > len(a) : return party_people(a[:-1]) 
        return len(a)
    return 0

