
def f(A, c):
    d = c**4 - 16*A**2
    if d < 0: return("Does not exist")
    b = ((c**2 + d**0.5)/2)**0.5
    a = 2*A/b
    return [round(a, 3), round(b, 3)]

