
def number_of_repeats(s):
    len_s = len(s)
    for k in range(1, len_s // 2 + 1):
        if not len_s % k:
            sub_s = s[:k]
            if all(s[i * k: (i + 1) * k] == sub_s
                   for i in range(1, len_s // k)):
                return len_s // k
    return 1

