
def is_shuffled_well(lst):
    j=1
    while j < len(lst)-1:
        if abs(lst[j] - lst[j - 1]) <= 1:
            if abs(lst[j] - lst[j + 1]) <= 1:
                return False
        j += 1
    return True

