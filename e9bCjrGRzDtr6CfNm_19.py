
def solve(a, b):
    if a == b:
        if b - 3*a + 4 == 0:
            return 'Any number'
        return 'No solution'
    return round((b - 3*a + 4) / (a - b), 3)

