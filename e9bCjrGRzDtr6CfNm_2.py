
def solve(a, b):
    if a == b and b - 3 * a + 4 == 0:
        return "Any number"
    elif a == b:
        return "No solution"
    return round((b - 3 * a + 4) / (a - b), 3)

