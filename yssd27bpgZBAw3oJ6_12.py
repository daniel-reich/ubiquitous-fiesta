
from math import factorial
​
def probability(u):
    return round(1 - factorial(365) / (factorial(365-u) * 365**u), 2)

