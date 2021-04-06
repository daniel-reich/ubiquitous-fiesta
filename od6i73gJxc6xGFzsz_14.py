
def is_slidey(n):
    l = list(map(int, str(n)))
    return all(map(lambda i: l[i] == l[i+1]+1 or l[i] == l[i+1]-1, range(len(l)-1)))

