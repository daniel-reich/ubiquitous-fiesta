
def f(A, c):
    try:
        a = round(((c**2 + 4*A)**0.5 + (c**2 - 4*A)**0.5)/2, 3)
        b = round(((c**2 + 4*A)**0.5 - (c**2 - 4*A)**0.5)/2, 3)
        return sorted((a, b))
    except TypeError:
        return 'Does not exist'

