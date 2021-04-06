
def n_differences(lst):
    a2 =[]
    c1 = lst.copy()
    while True:
        if len(c1)==1:break
        for i in range(len(c1)-1):
            a2.append(c1[i+1]-c1[i])
        c1 = a2
        a2=[]
    return c1[0]

