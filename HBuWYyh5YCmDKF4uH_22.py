
def almost_sorted(lst) :
    def chk_if_sorded(chk_lst):
        lst_chk = [(chk_lst[x] < chk_lst[x + 1]) for x in range(len(chk_lst) - 1)]
        if all(lst_chk) or not any(lst_chk) : return True
        return False
    if not chk_if_sorded(lst):
        for indx in range(len(lst)):
            n_lsr = lst.copy()
            n_lsr.pop(indx)
            if chk_if_sorded(n_lsr): return True
        return False
    else:return False

