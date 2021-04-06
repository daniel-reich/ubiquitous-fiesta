
def num_split(num):
    sign, lst = 1 if num >= 0 else -1, list(map(int,str(abs(num))))
    return [sign * lst[i] * 10**(len(lst)-i-1) for i in range(len(lst))]

