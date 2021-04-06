
def sorting_steps(lst):
    swaps = []
    goal = sorted(lst)
​
    if goal == lst:
        return []
​
    for limits in range(len(lst), 1, -1):  # bubbles you will do
        for index in range(1, limits):
            if lst[index] < lst[index-1]:
                lst[index], lst[index-1] = lst[index-1], lst[index]
                swaps.append((index, index-1))
​
    return swaps

