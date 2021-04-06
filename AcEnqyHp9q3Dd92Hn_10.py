
from functools import reduce
def multiply_nums(nums):
    return (
        reduce(lambda x, y: int(x) * int(y), nums.split(","))
        if len(nums.split(",")) > 1
        else int(nums)
    )

