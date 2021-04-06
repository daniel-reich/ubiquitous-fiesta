
def find_all_digits(nums):
    digits = list('0123456789')
    for n in nums:
        for d in str(n):
            if d in digits:
                digits.remove(d)
                if not digits:
                    return n
    return 'Missing digits!'

