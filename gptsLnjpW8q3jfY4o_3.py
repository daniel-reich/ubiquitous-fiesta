
from math import factorial as f
def Formula(n):
    if n==0:
        return '1'
    elif n==1:
        return 'a+b'
    elif n >= 2:
        s = ''
        for i in range(n+1):
            s += '+{}a^{}b^{}'.format(f(n)//(f(i)*f(n-i)), n-i, i)
        s = s.replace('a^1b', 'ab').replace('b^1+','b+').replace('a^0', '').replace('b^0', '').replace('+1b', '+b')
        return s[2:]
    else:
        return '1/({})'.format(Formula(-n))

