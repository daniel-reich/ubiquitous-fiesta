
def complete_bracelet(lst):
    sub = len(lst)
    i = 1
    while i + 1 < sub:
        i += 1
        if sub % i == 0:
            if lst[ : sub // i] * (i - 1) == lst[sub // i :]:
                return True
    return False

