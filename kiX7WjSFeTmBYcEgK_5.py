
def major_sum(lst):
    pos = neg = zero = 0
    for i in lst:
        if i > 0:
            pos += i
        elif i < 0:
            neg += i
        else:
            zero += 1
    return max((pos, neg, zero), key=abs)

