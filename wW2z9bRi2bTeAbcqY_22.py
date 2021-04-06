
def solve(a, b):
    # ax + 1 = b + x
    # ax - x = b - 1
    # x(a - 1) = b - 1
    # x = (b - 1) / (a - 1)
    if a==1 and b==1:
        return 'Any number'
    else:
        try:
            return round((b - 1) / (a - 1), 3)
        except:
            return 'No solution'

