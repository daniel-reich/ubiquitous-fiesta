
def solve(eq):
    x = eq.split()[1::]
    if x[0] == "-":
        return int(x[-1]) + int(x[1])
    else:
        return int(x[-1]) - int(x[1])

