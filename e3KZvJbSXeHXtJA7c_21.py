
def sum_missing_numbers(lst):
    lst.sort()
    total = 0
    for n in range(lst[0], lst[-1]):
        if n not in lst:
            total += n
    return total

