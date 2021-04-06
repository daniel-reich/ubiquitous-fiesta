
def difference_two(lst):
    diff = []
    for n1 in lst:
        for n2 in lst:
            if n1 - n2 == 2:
                diff.append([n2, n1])
    return sorted(diff)

