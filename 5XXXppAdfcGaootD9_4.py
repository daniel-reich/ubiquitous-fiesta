
def sum_odd_and_even(lst):
    even = odd = 0
    for x in lst:
        if x % 2:
            odd += x
        else:
            even += x
    return [even, odd]

