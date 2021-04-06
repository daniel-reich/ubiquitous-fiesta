
def sum_missing_numbers(lst):
    return sum([k for k in range(min(lst) + 1, max(lst)) if k not in lst])

