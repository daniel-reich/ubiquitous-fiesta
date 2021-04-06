
def get_discounts(nums, d):
    return [element * (int(d.strip("%")) / 100) for element in nums]

