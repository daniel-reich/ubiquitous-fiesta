
def kaprekar(num, n=0):
    if num == 6174:
        return n
    num = int(''.join(sorted([i for i in str(num)], reverse=True)))
    if num < 1000:
        num *= 10
    n += 1
    num_r = int(str(num)[::-1])
    diff = num - num_r
    if diff == 6174:
        return n
    else:
        return kaprekar(diff, n)

