
def lucky_seven(lst):
    lst = list(set(lst))
    n = len(lst)
    if n <= 2:
        return False
    for i in range(n):
        a = lst[i]
        for j in range(i + 1, n):
            b = lst[j]
            if 7 - a - b in lst[j+1:]:
                return True
    return False

