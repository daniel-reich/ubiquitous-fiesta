
def base_n(base, values, num):
    if len(values) != base:
        return False
​
    answ = []
    highest_multiple = 0
    for i in range(num):
        if (num // (base ** i)) < base:
            highest_multiple = base ** i
            break
​
    while highest_multiple >= 1:
        res = int(num // highest_multiple)
        answ.append(values[res])
        num -= res * highest_multiple
        highest_multiple /= base
    
    return ''.join([str(_) for _ in answ])

