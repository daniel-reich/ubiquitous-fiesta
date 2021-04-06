
def find_all_digits(nums):
    digits = []
    for num in nums:
        for i in str(num):
            if int(i) >= 0 and int(i) < 10 and i not in digits:
                digits.append(i)
            if sorted(digits) == ["0","1","2","3","4","5","6","7","8","9"]:
                return num
    return "Missing digits!"

