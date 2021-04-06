
def next_number(num):
    d1 = -1
    num = list(map(int, str(num)))
    for x in range(len(num)-1,-1,-1):
        if num[x] > num[x-1]:
            d1  = x - 1
            break
    if d1 == -1:
        return int(''.join(map(str, num)))
    d2 = d1 + 1
    for x in range(d2+1, len(num)):
        if num[x] < num[d2] and num[x] > num[d1]:
            d2 = x
    num[d1], num[d2] = num[d2], num[d1]
    return int(''.join(map(str, num[:d1+1]+sorted(num[d1+1:]))))

