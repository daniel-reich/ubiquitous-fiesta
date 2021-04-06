
def max_collatz(num):
    r = [num]
    while num != 1:
        if num % 2 == 0:
            num /= 2
            r.append(num)
        else:
            num = num * 3 + 1
            r.append(num)
    return max(r)

