
def solve(a, b):
    if (4 + b - 3 * a) == 0 and (a - b) == 0:
        return "Any number"
    try:
        return round((4 + b - 3*a) / (a - b), 3)
    except ZeroDivisionError:
        return "No solution"

