
def count_identical_lists(a, b, c, d):
    nested = (a, b, c, d)
    matched = max(nested.count(i) for i in nested)
    return matched if matched > 1 else 0

