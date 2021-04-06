
def sum_even_nums_in_range(start, stop):
    return sum(i for i in range(start, stop+1) if not i%2)

