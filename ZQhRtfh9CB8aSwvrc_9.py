
def greater_than_sum(nums):
    new = []
    sum = 0
    for i in range(len(nums)-1):
        sum += nums[i]
        if sum < nums[i+1]:
            new.append(True)
        else:
            new.append(False)
    return len(set(new)) == 1

