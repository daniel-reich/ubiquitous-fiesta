
def recaman_index(n):
    lst=[0]
    while True:
        m=lst[-1]-len(lst)
        a=lst[-1]+len(lst)
        if m>0 and m not in lst:
            lst.append(m)
            if m==n:
                break
            else:
                continue
        else:
            lst.append(a)
            if a==n:
                break
            else:
                continue
                
    return lst.index(n)

