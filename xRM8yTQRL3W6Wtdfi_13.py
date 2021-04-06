
def quartic_equation(a, b, c):
    D = (b**2) - (4*a*c)
    x = [(-b-(D**0.5))/2*a, (-b+(D**0.5))/2*a]
    set1 = {j for i in x for j in (i**0.5,-(i**0.5)) if i>=0}
    return len(set1)

