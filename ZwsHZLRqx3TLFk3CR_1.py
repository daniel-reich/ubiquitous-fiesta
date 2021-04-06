
def eval_factorial(lst):
    import math
    sum = 0
    for i in lst:
        sum += math.factorial(int(i[:-1]))
    return sum

