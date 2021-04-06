
def digit_count(n):
    str_n, rep_dict = str(n), dict()
    for c in str_n:
        if c in rep_dict:
            rep_dict[c] += 1
        else:
            rep_dict[c] = 1
    return int(''.join(str(rep_dict[c]) for c in str_n))

