
def kaprekar(num):
    count = 0
    while num != 6174:
        if len(str(num)) < 4:
            num *= 10 ** (4 - len(str(num)))
        if len(str(num)) == 4 and len({i for i in str(num)}) < 2:
            return None
        s = ''.join(sorted([i for i in str(num)]))
        num = int(s[::-1]) - int(s)
        count += 1
    return count

