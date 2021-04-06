
def covered_integers(lst):
    intervals = []
    for item in lst:
        for i in range(item[0], item[1]+1):
            intervals.append(i)
    sorted_intervals = set(sorted(intervals))
    return len(sorted_intervals)

