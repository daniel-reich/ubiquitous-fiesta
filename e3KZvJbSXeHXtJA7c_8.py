
def sum_missing_numbers(lst):
    temp = list(range(min(lst), max(lst)+1)) 
    return sum(i for i in temp if i not in lst)

