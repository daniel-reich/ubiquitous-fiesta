
def seven_segment(n):
    dig=('abcdef','bc','abdeg','abcdg','bcfg','acdfg','acdefg','abc','abcdefg','abcfg')
    ans=[]
    for i in range(len(n)-1):
        off=list(set(dig[int(n[i])]).difference(set(dig[int(n[i+1])])))     
        on=list(set(dig[int(n[i+1])]).difference(set(dig[int(n[i])])))
        on=[k.upper() for k in on]
        ans.append(sorted(off+on,key=str.casefold))
    return ans

