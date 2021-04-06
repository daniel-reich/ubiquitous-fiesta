
def find_all_digits(nums):
    digits = "0123456789"
    for i in nums:
        for j in str(i):
            if j in digits:
                digits = digits[:digits.index(j)]+digits[digits.index(j)+1:]
        if len(digits) == 0:
            return i
    return "Missing digits!"

