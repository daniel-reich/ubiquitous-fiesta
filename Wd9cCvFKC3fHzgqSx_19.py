
def num_split(num):
    x = []
    is_neg = False
    if num < 0:
        num *= -1
        is_neg = True
    y = str(num)
    for i in range(len(y)):
        x += [int(y[i]) * 10**(len(y)-i-1)]
    if is_neg:
        x = [-i for i in x]
    return x

