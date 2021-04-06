
def sentence_searcher(s, n):
    lst, idx, lst_idx = s[:-1].split(". "), 0, []
    for st in lst:
        idx += len(st.split(" "))
        lst_idx.append(idx)
    n += lst_idx[-1] if n < 0 else 0
    for i, st in enumerate(lst):
        if n < lst_idx[i]:
            return "{}.".format(st)
    return "n is out of range"

