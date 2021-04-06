
def is_special_array(lst):
    should_be_even = False
    for num in lst:
        if num % 2 != should_be_even:
            return False
        should_be_even = not should_be_even
    return True

