
def sum_missing_numbers(lst):
    lst = sorted(lst)
    print(lst)
    full_list = list(range(lst[0], lst[(len(lst)) -1]))
    sum = 0
    for val in full_list:
        if(val not in lst):
            sum += val
    return sum

