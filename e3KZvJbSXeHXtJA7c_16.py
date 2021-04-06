
def sum_missing_numbers(lst:list) -> int:
    range2set = list(range(min(lst), max(lst)+1) )
    return sum(list(set(range2set) - set(lst)))

