
def get_subsets(lst, n):
    if not lst:
        return []
    current, *rest = lst
    result = [[current]] if current == n else []
    if current < n:
        result += [sub+[current] for sub in get_subsets(rest, n-current)]
        result += get_subsets(rest, n)
    return sorted([sorted(sub) for sub in result], key=lambda x: (len(x), x[0]))

