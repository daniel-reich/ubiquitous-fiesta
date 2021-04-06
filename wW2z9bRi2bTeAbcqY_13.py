
def solve(a,b):
    if a == 1 and b == 1:
        return "Any number"
    elif a == 1 and b !=1:
        return "No solution"
    else:
        return round((b - 1) / (a - 1), 3)

