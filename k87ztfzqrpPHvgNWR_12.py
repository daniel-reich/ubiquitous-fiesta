
def widen_streets(lst, n):
    new = ['']*len(lst)
    for i in range(len(lst)):
        for ind,j in enumerate(lst[i]):
            if lst[-1][ind]=='#': new[i]+=j
            else: new[i]+=' '*n
​
    return new

