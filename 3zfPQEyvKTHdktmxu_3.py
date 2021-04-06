
def big_sub(lst):
    best_sum = 0
    best_start, best_end = 0, 0
    cur_sum = 0
    for cur_end, x in enumerate(lst):
        if cur_sum <= 0:
            cur_start = cur_end
            cur_sum = x
        else:
            cur_sum += x
        if cur_sum >= best_sum:
            best_sum = cur_sum
            best_start = cur_start
            best_end = cur_end
    return [best_sum, best_start, best_end]

