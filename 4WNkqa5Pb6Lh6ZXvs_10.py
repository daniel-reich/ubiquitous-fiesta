
allowed = "0123456789()+-*/^x"
def evaluate_polynomial(poly, num):
    if any([c not in allowed for c in poly]) or len(poly.strip()) == 0:
        return "invalid"
    poly = poly.replace('^', '**').replace('x(', 'x*(').replace('/', '//')
    for d in range(10):
        poly = poly.replace(str(d) + '(', str(d) + '*(')
        poly = poly.replace(str(d) + 'x', str(d) + '*x')
    poly = poly.replace('x', str(num))
    try:
        ans = eval(poly)
        return ans
    except:
        return "invalid"

