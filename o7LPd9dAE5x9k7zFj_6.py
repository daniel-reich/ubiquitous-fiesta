
from math import log
def logarithm(base, num):
    try:
        return log(num)/log(base)
    except (ValueError, ZeroDivisionError):
        return "Invalid"

