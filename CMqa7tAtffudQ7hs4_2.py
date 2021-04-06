
def sorting_steps(lst):
    lst = lst[:]
    swaps = []
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        if i != min_index:
            swaps.append((i, min_index))
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return swaps

