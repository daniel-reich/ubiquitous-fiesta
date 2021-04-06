
def solve(a, b):
    if (a - b) != 0:
        result = (b - 3*a + 4) / (a - b)
        return round(result, 3)
    elif a == b == 2:
        return "Any number"
    else:
        return "No solution"

