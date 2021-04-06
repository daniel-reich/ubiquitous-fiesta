
def almost_sorted(lst):
    compare = [lst[i - 1] < lst[i] for i in range(1, len(lst))]
    if compare.count(True) == 1:
        idx = compare.index(True)
        if (lst[:idx] + lst[idx + 1:]
                == sorted(lst[:idx] + lst[idx + 1:], reverse=True) or
            lst[:idx + 1] + lst[idx + 2:]
                == sorted(lst[:idx + 1] + lst[idx + 2:], reverse=True)):
            return True
    elif compare.count(False) == 1:
        idx = compare.index(False)
        if (lst[:idx] + lst[idx + 1:]
                == sorted(lst[:idx] + lst[idx + 1:]) or
                lst[:idx + 1] + lst[idx + 2:]
                == sorted(lst[:idx + 1] + lst[idx + 2:])):
            return True
    else:
        return False

