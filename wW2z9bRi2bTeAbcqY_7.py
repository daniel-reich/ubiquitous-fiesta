
def solve(a,b):
    if a == 1 and b == 1:
        return "Any number"
    else:
        try:
            first = a - 1
            second = -1 + b
            third = round(second / first,3)
            return third
        except ZeroDivisionError:
            return "No solution"

