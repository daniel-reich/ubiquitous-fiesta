
def consecutive_combo(list1, list2):
    x = list1 + list2
    x.sort()
    for i in range(0, len(x) - 1):
        if x[i + 1] - x[i] != 1:
            return False
    return True

