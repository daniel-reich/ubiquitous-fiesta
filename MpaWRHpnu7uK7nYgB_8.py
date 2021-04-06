
def doubleton(n):
    for h in range(n+1,n+200):
        if len(set(str(h)))==2:
            return h

