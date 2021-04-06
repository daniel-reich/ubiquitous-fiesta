
def meme_sum(a, b):
    s_a, s_b = str(a), str(b)
    len_a, len_b = len(s_a), len(s_b)
    max_len = max(len_a, len_b)
    lst_a = [0] * (max_len - len_a) + list(map(int, list(s_a)))
    lst_b = [0] * (max_len - len_b) + list(map(int, list(s_b)))
    return int("".join(str(i + j) for i, j in zip(lst_a, lst_b)))

