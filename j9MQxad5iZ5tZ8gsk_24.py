
import math
def find_vertex(equation):
    x = equation.split('x')
    b = x[1]
    a = x[0]
    b = int(b.replace('+','').strip()) * -1
    a = int(a.strip())
    c = math.floor(b / (2 * a))
    return c

