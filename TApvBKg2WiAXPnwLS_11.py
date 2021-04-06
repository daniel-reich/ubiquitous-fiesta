
def nth_smallest(lst, n):
    number_of_values = 0
    for valus in lst:
        number_of_values += 1
    if  n == None or n <= 0 or n > number_of_values or n == None:
        return None
    else:
        new_list = sorted(lst)
        return new_list[n-1]

