
def last(a, n):
    if n<=len(a):
        return a[len(a)-n:]
    elif n>len(a):
        return 'invalid'
    else:
        return []

