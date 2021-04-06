
def solve(a, b):
    if a == b == 2:
        return "Any number"
    elif a == b != 2:   
        return "No solution"
    else:
        result = (b - 3*a + 4) / (a - b)
        return round(result, 3)

