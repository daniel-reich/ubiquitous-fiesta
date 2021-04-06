
def numbers_to_ranges(lst):
    if not lst: return []
    if len(lst) == 1: return [str(lst[0])]
    solution, start = list(), lst[0]
    for i in range(1, len(lst)):
        if lst[i] != lst[i-1] + 1:
            if start != lst[i-1]:
                solution.append(str(start)+"-"+str(lst[i-1]))
            else:
                solution.append(str(start))
            start = lst[i]
    return solution+[str(start)+"-"+str(lst[i])]

