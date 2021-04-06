
def solve(a, b):
    if a == 1:
        return "Any number" if b == 1 else "No solution"
    return round((b - 1) / (a - 1.), 3)

