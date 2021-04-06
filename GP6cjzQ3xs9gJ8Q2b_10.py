
def is_polydivisible(n):
    if n == 0:
        return True
    num_len = len(str(n))
    string_n = str(n)
    for x in range(1, num_len+1):
        y = int(string_n[0:x])
        if y % x != 0:
            return False
    return True

