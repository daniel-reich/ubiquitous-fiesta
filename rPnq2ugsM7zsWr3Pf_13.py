
def find_all_digits(nums):
    digits = list(map(str, range(10)))
    for num in nums:
        for digit in str(num):
            if digit in digits:
                digits.remove(digit)
                if not digits:
                    return num
    return 'Missing digits!'

