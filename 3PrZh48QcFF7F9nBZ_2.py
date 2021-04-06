
def solver(eq):
    eq = eq.replace(" -", " + -").replace(' x', '1*x')
    side1, side2 = eq.split('=')
    coeff1 = [sum(eval(t.replace('*x', '')) for t in side1.split('+') if '*x' in t and '*x*' not in t),
              sum(eval(t.replace('*x', '')) for t in side1.split('+') if '*x' not in t)]
    coeff2 = [sum(eval(t.replace('*x', '')) for t in side2.split('+') if '*x' in t and '*x*' not in t),
              sum(eval(t.replace('*x', '')) for t in side2.split('+') if '*x' not in t)]
    return (coeff2[1]-coeff1[1])/(coeff1[0]-coeff2[0]) if coeff1[0]!=coeff2[0] else 'Infinite solutions'

