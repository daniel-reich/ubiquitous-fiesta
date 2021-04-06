
def digit_occurrences(s,n,d):
    return ''.join([str(i) for i in range(s,n+1)]).count(str(d))

