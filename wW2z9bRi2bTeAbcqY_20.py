
def solve(a,b):
    if a != 1:
        return round((b-1)/(a-1), 3)
    elif b != 1:
        return "No solution"
    else:
        return "Any number"

