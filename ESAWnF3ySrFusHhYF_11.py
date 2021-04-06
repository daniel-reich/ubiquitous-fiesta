
def edit_words(lst):
    res = []
    for w in lst:
        len_w = len(w)
        len_w2 = len_w // 2 + 1 if len_w % 2 else len_w // 2
        up_w = w.upper()[::-1]
        res.append("-".join([up_w[:len_w2], up_w[len_w2:]]))
    return res

