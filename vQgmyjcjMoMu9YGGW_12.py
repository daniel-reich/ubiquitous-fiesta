
def simplify(txt):
    from fractions import Fraction as frac
    inp = txt.split('/')
    result = str(frac(int(inp[0]), int(inp[1])))
    return result

