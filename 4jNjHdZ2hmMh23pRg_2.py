
def cutting_grass(lst, *cuts):
    s=[lst]
    T=False
    for i in cuts:
        s1=s[-1][:]
        if T or min(s1)<=i:
            T=True
            s.append("Done")
        else :
            for j in range(len(lst)):
                s1[j]-=i
            s.append(s1)
    return s[1:]

