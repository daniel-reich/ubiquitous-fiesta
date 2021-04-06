
def greater_than_sum(nums):
    lst1=[True for x in range(1,len(nums)) if sum(nums[:x])<nums[x]]
    return (len(nums)-1)==len(lst1)

