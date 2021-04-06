
def is_undulating(n):
    l=len(str(n))
    sn=str(n)
    if (l<3) | len(set(sn))!=2:
        return False
    else:
        for i in range(0,l-2,2):
            if sn[i]==sn[i+1]:
                return False
            elif sn[i]==sn[i+2]:
                    continue
            else:
                return False
        return True

