
def reversible_inclusive_list(start_of_range, end_of_range):
    x = -1 if start_of_range > end_of_range else 1
    incl_nums = [i for i in range(start_of_range, end_of_range, x)] + [end_of_range]
    return incl_nums

