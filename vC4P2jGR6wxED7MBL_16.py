
def larger_than_right(lst):
    results = []
    for i, num in enumerate(lst):
        if i == len(lst) - 1 or all([num > j for j in lst[i + 1:]]):
            results.append(num)
    return results

