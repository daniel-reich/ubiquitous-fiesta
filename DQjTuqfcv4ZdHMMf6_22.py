
def kaprekar(num, c=0):
    if num == 6174:
        return c
    num = [num, int(str(num) + '0')][num < 1000]
    high = int(''.join(sorted(str(num), reverse=True)))
    low = int(''.join(sorted(str(num))))
    return kaprekar(high - low, c + 1)

