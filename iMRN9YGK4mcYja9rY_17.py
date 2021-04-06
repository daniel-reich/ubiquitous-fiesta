
def accumulating_product(lst):
    current = 1
    accumulated = []
    for item in lst:
        current_value = item * current
        current = current_value
        accumulated.append(current_value)
    return accumulated

