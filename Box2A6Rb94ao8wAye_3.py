
def leader(lst):
    return [e for i, e in enumerate(lst) if all(e > a for a in lst[:i:-1])]

