
def GCD(lst):
    state = True
    if min(lst) > 1:
        for i in range(min(lst), 1, -1):
            for j in lst:
                if j % i != 0:
                    state = False
            if state:
                return i
            else:
                state = True
        return 1
    else:
        return 1

