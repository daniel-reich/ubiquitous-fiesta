
def diagonalize(n, d):
    lst = [[i for i in range(i, i+n)] for i in range(n)]
    if d == 'ul':
        return lst
    elif d == 'ur':
        return [sorted(i, reverse=True) for i in lst]
    elif d == 'll':
        return sorted(lst, reverse=True)
    elif d == 'lr':
        return sorted([sorted(i, reverse=True) for i in lst], reverse=True)

