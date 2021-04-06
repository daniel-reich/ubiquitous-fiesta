
def is_consecutive(s):
    len_s = len(s)
    for size in range(1, len_s // 2 + 1):
        if not len_s % size:
            lst = [int(s[k * size: (k + 1) * size])
                   for k in range(len(s) // size)]
            if (all(a - b == 1 for a, b in zip(lst, lst[1:])) or
                    all(b - a == 1 for a, b in zip(lst, lst[1:]))):
                return True
    return False

