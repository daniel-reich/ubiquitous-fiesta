
def non_repeats(radix):
    count = 0
    for num_digits in range(1, radix + 1):
        product = radix - 1
        for i in range(1, num_digits):
            product *= (radix - i)
        count += product
    return count

