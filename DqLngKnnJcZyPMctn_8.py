
def stock_picker(lst):
    p_list = [max(lst[i + 1:]) - lst[i] for i in range(0, len(lst) - 1)]
    return max(p_list) if max(p_list) >= 0 else -1

