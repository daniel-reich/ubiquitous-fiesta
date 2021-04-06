
def multiply_nums(nums):
    nums = "".join(nums.split())
    nums = nums.split(',')
    print(nums)
    a = [int(i) for i in nums]
    #print(a)
    p = 1
    for i in a:
        p *= i
    return p

