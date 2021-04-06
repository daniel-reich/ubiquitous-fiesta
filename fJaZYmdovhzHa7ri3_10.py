
def max_collatz(num):
    if num == 1:
        return num
    r = []
    while num != 1:
        r.append(num)
        if num % 2 == 0:
            num = num // 2
        else:
            num = (num * 3) + 1
    return max(r)

