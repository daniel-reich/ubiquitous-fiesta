
def bemirp(p):
    def is_prime(p):
        return p>0 and all(p%ii for ii in range(2,int(p**0.5)+1))
    if is_prime(p):
        e = str(p)[::-1]
        if int(e) != p and is_prime(int(e)):
            trans = {'6': '9', '9': '6'}
            b1 = ''.join(trans.get(dig, dig) for dig in str(e))
            b2 = ''.join(trans.get(dig, dig) for dig in str(p))
            if is_prime(int(b1)) and is_prime(int(b2)):
                return 'B'
            return 'E'
        return 'P'
    return 'C'

