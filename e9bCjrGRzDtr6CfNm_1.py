
def solve(a, b):
    if -3*a + b + 4 == 0 or -3*a + b + 4 == 0 and a == b:
        return("Any number")
    elif a == b:
        return "No solution" 
    else:
        return round((-3*a + b + 4)/(a-b), 3)

