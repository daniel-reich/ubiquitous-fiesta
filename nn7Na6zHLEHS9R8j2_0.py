
def deep_count(lst):
    if not isinstance(lst, list):
        return 0
    return len(lst) + sum(map(deep_count, lst))

