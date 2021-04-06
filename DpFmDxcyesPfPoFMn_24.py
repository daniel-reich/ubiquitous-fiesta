
def isbn13(txt):
    key = [[10,9,8,7,6,5,4,3,2,1], [1,3,1,3,1,3,1,3,1,3,1,3,1]]
    is13 = len(txt) == 13
    lst = [10 if d=='X' else int(d) for d in txt]
    s = sum(d * k for d,k in zip(lst, key[is13]))
    if is13: return 'Invalid' if s%10 else 'Valid'
    if s%11: return 'Invalid'
    lst = [9,7,8] + lst[:-1] + [0]
    s = sum(d * k for d,k in zip(lst, key[1]))
    r = s % 10
    lst[12] = 10 - r
    return ''.join(str(d) for d in lst)

