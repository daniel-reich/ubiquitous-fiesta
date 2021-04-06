
def sum_missing_numbers(lst):
    s = set(lst)
    return sum(i for i in range(min(s), max(s)) if i not in s)

