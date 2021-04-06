
def get_discounts(nums, d):
        return [e* int(d.strip("%"))/100 for e in nums]

