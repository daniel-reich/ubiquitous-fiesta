
def find_all_digits(nums):
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
​
    i = 0
    while i < len(nums) and digits:
        curr_num = [int(x) for x in str(nums[i])]
        for n in curr_num:
            if n in digits:
                digits.remove(n)
        if not digits:
            return nums[i]
        i += 1
​
    return 'Missing digits!' if digits else nums[i]

