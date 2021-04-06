
def fib(n):
    pre_0 = 0
    pre_1 = 1
    pre_2 = 1
    if n == 1: return pre_1
    elif n == 0: return pre_0
    for i in range(1, n):
        pre_2 = pre_0 + pre_1
        pre_0 = pre_1
        pre_1 = pre_2
    return pre_2

