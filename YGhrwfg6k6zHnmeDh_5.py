
def get_discounts(nums, d):
    return list(map(lambda x : x * int(d[:-1]) / 100, nums))

