
def get_only_evens(nums):
    return [value for index, value in enumerate(nums) if not index%2 and not value%2]

