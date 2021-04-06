
def full_cycle(lst):
    len_lst = len(lst)
    not_visit = [True] * len_lst
    idx = lst[0]
    while any(not_visit):
        if -1 < idx < len_lst and not_visit[idx]:
            not_visit[idx] = False
            idx = lst[idx]
        else:
            return False
    return True

