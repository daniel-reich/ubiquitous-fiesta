
def split_n_cases(s, cases):
    len_s = len(s)
    if not len_s % cases:
        sub_len = len_s // cases
        return [s[i: i + sub_len] for i in range(0, len_s, sub_len)]
    return ['Error']

