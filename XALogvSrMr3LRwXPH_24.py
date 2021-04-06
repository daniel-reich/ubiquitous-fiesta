
def is_shuffled_well(lst):
    c = 0
    for i in range(len(lst) - 2):
        if lst[i] + 1 == lst[i + 1] or lst[i + 1] + 1 == lst[i]:
            c += 1
        else:
            c = 0
        if c >= 2:
            return False
    return True

