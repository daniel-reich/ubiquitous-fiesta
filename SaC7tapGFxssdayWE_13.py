
def find_vertex(a, b, c):
    x = -(b/(2*a))
    y = a*(x**2) + b*x + c
    return [x, y]

