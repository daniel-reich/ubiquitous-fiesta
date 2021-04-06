
def pop(lst):
    if len(lst) <= 1:
        return lst
    mx = max(lst)
    return [i for i in range(mx)] + [mx] + [i for i in range(mx)][::-1]

