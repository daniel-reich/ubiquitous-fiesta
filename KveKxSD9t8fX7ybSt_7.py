
def final_countdown(lst):
    r = []
    lst = lst[::-1]
    while True:
        if 1 in lst:
            i = lst.index(1)
        else:
            r = r[::-1]
            r = [len(r)] + [r]
            return r
        lst = lst[i:]
        i = 1
        while len(lst) > 1 and lst[i] - 1 == lst[i - 1]:
            i += 1
            if i == len(lst):
                break
        r += [lst[: i][::-1]]
        lst = lst[i :]

