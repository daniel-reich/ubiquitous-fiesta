
def is_shuffled_well(lst):
    for i in range(8):
        diff = (lst[i] - lst[i+1], lst[i+1] - lst[i+2])
        if diff in ((-1, -1), (1, 1)):
            return False
    return True

