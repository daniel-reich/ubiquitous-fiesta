
def pluralize(lst):
    from collections import Counter
    dict_ = Counter(lst)
    lst_out = []
    for k, v in dict_.items():
        if v > 1:
            lst_out.append(k+"s")
        else:
            lst_out.append(k)
    return set(lst_out)

