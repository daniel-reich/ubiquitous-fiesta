
def round_number(num, n):
    if num % n == 0:
        return num
    k = num / n
    n1 = int(k) * n
    n2 = (int(k) + 1) * n
    return n1 if num - n1 < n2 - num else n2

