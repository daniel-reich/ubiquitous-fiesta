
def reversible_inclusive_list(start, end, step=None):
    if step is None:
        step = 1 if start <= end else -1
    return ([start] + reversible_inclusive_list(start + step, end, step)
            if start != end + step else [])

