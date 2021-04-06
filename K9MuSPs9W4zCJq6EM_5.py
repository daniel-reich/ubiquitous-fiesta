
def cycle_length(lst, n):
    srt_lst = sorted(lst)
    i = 0
    while True:
        if lst.index(n) == srt_lst.index(n):
            break
        else:
            new = lst[srt_lst.index(n)]
            lst[lst.index(n)] ,lst[srt_lst.index(n)]= lst[srt_lst.index(n)], lst[lst.index(n)]
            i += 1
            n = new
    return i

