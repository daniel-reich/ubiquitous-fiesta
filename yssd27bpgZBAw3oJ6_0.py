
from math import factorial as f
​
def probability(u):
    return round(1 - (f(365)/f(365-u))/365**u, 2)

