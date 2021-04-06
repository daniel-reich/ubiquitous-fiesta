
def f(A, c):
    p1 = (c**4 - 16*(A**2))
    return "Does not exist" if p1<0 else sorted([round(((c**2 + p1**0.5)/2)**0.5,3),round(((c**2 - p1**0.5)/2)**0.5,3)])

