
def makeBox(n):
    if n == 1:
        return ['#']
    lst = []
    top = '#' * n
    mid = '#' + (n-2)*' ' + '#'
    lst.append(top)
    for x in range(n-2):
        lst.append(mid)
    lst.append(top)
    return lst

