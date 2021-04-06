
def jumping_frog(n, stones):
    s=2
    p=stones[0]
    while p<n:
        ahead=back=0
        if p-stones[p]>=0:
            back=stones[p-stones[p]]-stones[p]
        if p+stones[p]<n:
            ahead=stones[p]+stones[p+stones[p]]
        else:
            return s+1
        if (ahead>=back and stones[p+stones[p]]!=0) or stones[p-stones[p]]==0:
            p+=stones[p]
            s+=1
        else:
            p-=stones[p]
            s+=1
        if p+stones[p]<n and stones[p+stones[p]]==0:
            return 'no chance :-('
    return s+1

