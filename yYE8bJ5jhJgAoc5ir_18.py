
def bugger(num):
    num, count = str(num), 0
    while len(num) > 1:
        count += 1
        a = 1
        for i in num:
            a *= int(i)
        num = str(a)
    return count

