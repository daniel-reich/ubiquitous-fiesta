
def int_within_bounds(n, lower, upper):
    number = []
    for i in range(lower, upper):
        number.append(i)
    if n in number:
        return True
    else:
        return False

