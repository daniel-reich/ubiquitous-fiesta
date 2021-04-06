
def hex_lattice(n):
    ans=''
    p=(3+(12*n-3)**.5)/6
    if not p.is_integer():
        return 'Invalid'
    rows=0;ds=-1;dc=1;cc=int(p)-1;sc=int(p)
    while rows<2*int(p)-1:
        ans+=' '*sc+'o '*cc+'o'+' '*sc+'\n'
        sc+=ds
        cc+=dc
        rows+=1
        if sc==1:
            ds=1
            dc=-1
    return ans[:-1]

