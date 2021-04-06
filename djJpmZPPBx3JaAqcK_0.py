
def maya_number(n):
    if n == 0:
        return ['@']
    
    res = []
    while n:
        if n%20:
            lines, dots = divmod(n%20, 5)
            res.append('{}{}'.format('o'*dots, '-'*lines))
        else:
            res.append('@')
        n //= 20
        
    return res[::-1]

