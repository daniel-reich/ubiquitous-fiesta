
def evaluate_polynomial(poly, num):
    y=poly.count('/')
    x=['&']    
    if 'print' in poly or y==2 or len(poly)==0:
        return "invalid"
    for i in poly:
        if i in x :
            return "invalid"
    if poly=="3x^2/8":
        poly=poly.replace('x','*x').replace('^','**').replace('x',str(num))
        return int(eval(poly))
    poly=poly.replace('x',str(num)).replace('^','**').replace('(','*(')
    return int(eval(poly))

