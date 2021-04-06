
def convert(deg):
    C = lambda c: str(int(round(int(c) * 1.8 + 32))) + '*F'
    F = lambda f: str(int(round((int(f) - 32) / 1.8))) + '*C'
    return eval(deg[-1])(deg.split('*')[0]) if '*' in deg else 'Error'

