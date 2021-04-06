
def largest_even(lst):
    largest_so_far = -1
    for num in lst:
        if num % 2 == 0:
            if num > largest_so_far:
                largest_so_far = num
    return largest_so_far

