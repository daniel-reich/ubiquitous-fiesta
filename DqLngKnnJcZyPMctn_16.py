
def stock_picker(lst):
    diffs = [lst[i] - lst[i - 1] for i in range(1, len(lst))]
    max_diff = acc_diffs = 0
    increasing = False
    for d in diffs:
        if d >= 0:
            if increasing:
                acc_diffs += d
            else:
                acc_diffs = d
                increasing = True
        else:
            increasing = False
        if acc_diffs > max_diff:
            max_diff = acc_diffs
    return max_diff if max_diff else -1

