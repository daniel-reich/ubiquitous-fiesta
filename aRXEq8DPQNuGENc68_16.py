
from math import e
def salt(t):
    return round(1 + 9 * e**(-t/10), 3)

