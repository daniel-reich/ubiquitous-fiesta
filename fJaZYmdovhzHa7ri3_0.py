
def max_collatz(num):
    res = num
    while num > 1:
        num = num * 3 + 1 if num % 2 else num // 2
        if num > res:
            res = num
    return res

