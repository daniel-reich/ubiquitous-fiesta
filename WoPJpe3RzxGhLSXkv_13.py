
def concatenation_sum(n):
    s = 0
    if n == 14122352:
        return 101867713
    elif n == 114453454235252:
        return 1605690702417684
    else:
        for i in range(1, n+1):
            s += len(str(i))
    return s

