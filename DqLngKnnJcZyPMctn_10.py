
def stock_picker(lst):
    if sorted(lst, reverse=True) == lst:
        return -1
​
    max_profit = 0
    for i, x in enumerate(lst):
        diff = max(lst[i + 1:], default=0) - x
        if diff > max_profit:
            max_profit = diff
​
    return max_profit

