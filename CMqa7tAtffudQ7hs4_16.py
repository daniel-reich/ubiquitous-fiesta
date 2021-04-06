
def sorting_steps(lst):
    swaps, arr = [], lst[:]
    for i, j in zip(sorted(arr), arr):
        if i != j:
            a, b = arr.index(i), arr.index(j)
            arr[a], arr[b] = arr[b], arr[a]
            swaps.append((b, a))
    return swaps
quit()

