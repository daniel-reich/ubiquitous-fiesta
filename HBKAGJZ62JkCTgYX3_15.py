
def last(l,n):
    if n>len(l):
        return 'invalid'
    elif n==0:
        return []
    else:
        return l[len(l)-n:]

