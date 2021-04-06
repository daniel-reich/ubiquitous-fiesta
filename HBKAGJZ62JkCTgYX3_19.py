
def last(a, n):
    return [a[i] for i in range(len(a)-n,len(a))] if n <= len(a) else "invalid"

