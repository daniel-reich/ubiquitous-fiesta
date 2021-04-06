
def find_all_digits(nums):
    all_digits = list(range(10))
    for num in nums:
        for digit in str(num):
            if int(digit) in all_digits:
                all_digits.remove(int(digit))
            if len(all_digits) == 0:
                return num
    return "Missing digits!"

