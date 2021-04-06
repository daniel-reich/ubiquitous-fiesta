
def missing_alphabets(s):
    repeat = max(s.count(i) for i in set(s))
    res = ''
    for i in 'abcdefghijklmnopqrstuvwxyz':
        res += i * (repeat - s.count(i))
    return res

