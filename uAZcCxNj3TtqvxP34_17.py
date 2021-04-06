
def mode(nums):
    result = [nums[0]]
    cnt = nums.count(nums[0])
    for num in nums:
        if nums.count(num) > cnt:
            result = []
            result.append(num)
            cnt = nums.count(num)
        elif nums.count(num) == cnt:
                  result.append(num)
    return sorted(set(result))

