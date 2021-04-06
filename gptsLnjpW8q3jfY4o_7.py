
def Formula(n):
    if not n: return '1'
    Formula, sign, res = str(), n < 0, 1
    if sign: n = -n
    for i in range(n + 1):
        if i % n: 
            res = int(res * (n - i + 1) / i)
            Formula += str(res)
        if i < n: Formula += 'a'
        if i < n - 1: Formula += '^' + str(n - i)
        if i > 0: Formula += 'b'
        if i > 1: Formula += '^' + str(i)
        if i < n: Formula += '+'
    return ('1/(' + Formula + ')' if sign else Formula)

