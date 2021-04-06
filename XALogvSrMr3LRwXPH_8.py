
def is_shuffled_well(lst):
    count_up, count_down = 0, 0
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1] + 1:
            count_up += 1
            count_down = 0
        elif lst[i] == lst[i - 1] - 1:
            count_down += 1
            count_up = 0
        else:
            count_up, count_down = 0, 0
        if count_up == 2 or count_down == 2:
            return False
    return True

