
def maya_number(n):
    res = []
    while n:
        d = n % 20
        res.insert(0, 'o'*(d%5) + "-"*(d//5) if d else '@')
        n //= 20
    return res or ['@']

