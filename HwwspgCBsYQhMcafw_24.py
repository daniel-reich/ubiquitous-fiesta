
def super_digit(n, rep):
    num = str(n)*rep
    #num = int(num)
    while len(num) > 1:
        total = 0
        for i in num:
            total += int(i)
        num = str(total)
    return int(num)

