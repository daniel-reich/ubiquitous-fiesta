
def landscape_type(lst):
    mx, mn = max(lst), min(lst)
    pmx = lst.index(mx)
    pmn = lst.index(mn)
    # mountain
    if all(lst[i] >= lst[i-1] for i in range(1, pmx)) and \
       all(lst[i] <= lst[i-1] for i in range(pmx+1, len(lst))):
        return "mountain" if mx not in (lst[0], lst[-1]) else "neither"
    # valley
    if all(lst[i] <= lst[i-1] for i in range(1, pmn)) and \
       all(lst[i] >= lst[i-1] for i in range(pmn+1, len(lst))):
        return "valley" if mn not in (lst[0], lst[-1]) else "neither"
    return "neither"

