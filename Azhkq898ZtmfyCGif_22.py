
def numbers_to_ranges(lst):
    if lst==[]:return []
    s=e=lst[0]
    r=[]
    for i in range(len(lst)-1):
        if lst[i]+1==lst[i+1]:
            e=lst[i+1]
        else:
            r.append(str(s)+1*(s!=e)*('-'+str(e)))
            s=e=lst[i+1]
    r.append(str(s)+1*(s!=e)*('-'+str(e))) 
    return r

