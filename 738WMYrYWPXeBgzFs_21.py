
def is_valid(txt):
    c = sorted([txt.count(i) for i in set(txt)])
    if all(c[i] == c[i+1] for i in range(len(c)-1)):
        return 'YES'
    elif all(c[i] == c[i+1] for i in range(1,len(c)-1)) and c[1]-c[0] == 1:
        return 'YES'
    elif all(c[i] == c[i+1] for i in range(len(c)-2)) and c[-1]-c[-2] == 1:
        return 'YES'
    return 'NO'

