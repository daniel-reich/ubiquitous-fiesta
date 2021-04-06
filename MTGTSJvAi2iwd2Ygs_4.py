
def valid_division(d):
    a, b = map(int, d.split('/'))
    if b == 0:
        return 'invalid'
    res = a / b
    if str(res)[str(res).index('.')+1:] == '0':
        return True
    else:
        return False

