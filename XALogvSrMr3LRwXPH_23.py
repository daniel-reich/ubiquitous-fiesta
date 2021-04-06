
def is_shuffled_well(lst):
    
    for i in range(len(lst) - 2):
        if abs(lst[i + 1] - lst[i]) == 1 and abs(lst[i + 2] - lst[i + 1]) == 1:
            return False
    return True

