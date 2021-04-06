
def priority_sort(lst, s):
    if not lst and not s:
        return []
    if not s:
        return sorted(lst)
    return sorted([n for n in lst if n in s]) + sorted([m for m in lst if m not in s])

