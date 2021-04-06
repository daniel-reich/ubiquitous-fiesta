
def iso_group(lst):
    if lst.count(max(lst))==1: return max(lst)
    else:
        a=[]
        for i in range(lst.count(max(lst))):
            a.append(max(lst))
        return(a)

