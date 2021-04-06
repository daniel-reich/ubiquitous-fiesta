
def evaluate_polynomial(poly, num):
    a = ['0','1','2','3','4','5','6','7','8','9','x','(',')','/','*','+','-','^']
    x = num
    for i in range(len(poly)):
        if poly[i] not in a:
            return 'invalid'
    if '//' in poly:
        return 'invalid'
    poly = poly.replace('^','**')
    poly = poly.replace('(','*(')
    poly = poly.replace('2x','2*x')
    poly = poly.replace('3x','3*x')
    poly = poly.replace('4x','4*x')
    poly = poly.replace('5x','5*x')
    poly = poly.replace('6x','6*x')
    poly = poly.replace('7x','7*x')
    poly = poly.replace('8x','8*x')
    poly = poly.replace('9x','9*x')
    poly = poly.replace('0x','0*x')
    poly = poly.replace('/','//')
    if len(poly) == 0:
        return 'invalid'
    return eval(poly)

