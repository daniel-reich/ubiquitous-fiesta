
def almost_sorted(lst: list) -> bool:
    tot_increasing, tot_decreasing = 0, 0
    for i in range(1, len(lst)):
        if lst[i] >= lst[i-1]:
            tot_decreasing += 1
        elif lst[i-1] >= lst[i]:
            tot_increasing += 1
    return min(tot_decreasing, tot_increasing) == 1

