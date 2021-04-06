
def find_all_digits(nums):
    missing = set(range(10))
    for n in nums:
        m = n
        while m > 0:
            digit = m % 10
            m //= 10
            if digit in missing:
                missing.remove(digit)
                if len(missing) == 0:
                    return n
    return "Missing digits!"

