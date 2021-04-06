
def block(lst):
    sum1 = 0
    for i in range(len(lst)):
        sum1 += (len(lst) - i - 1) * ''.join(str(j) for j in lst[i]).count('2')
    return sum1

