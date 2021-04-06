
import math
def find_vertex(x):
    a, b, c = [int(f(s)) for s in x.split('x')]
    return math.floor(-b / (2*a))
​
def f(s):
    return ''.join([c for c in s if c in '-0123456789'])

