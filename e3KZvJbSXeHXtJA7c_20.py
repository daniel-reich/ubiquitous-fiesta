
def sum_missing_numbers(lst):
    highest_num = max(lst)
    lowest_num = min(lst)
    return sum([i for i in range(lowest_num + 1, highest_num) if i not in lst])

