
def who_goes_free(n, k):
    lst = list(range(n))
    while len(lst) > 1:
        for i in range(k - 1):
            lst = lst[1:] + [lst[0]]
        lst = lst[1:]
    return lst[0]

