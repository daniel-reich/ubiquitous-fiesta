
def sum_odd_and_even(lst):
    odd, even = 0, 0
    for i in lst:
        if i%2:
            odd += i
        else:
            even += i
    return [even, odd]

