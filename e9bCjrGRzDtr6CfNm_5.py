
def solve(a,b):
    if a != b :
        return round((b - 3 * a + 4)/(a - b), 3)
    elif a != 2:
        return "No solution"
    else:
        return "Any number"

