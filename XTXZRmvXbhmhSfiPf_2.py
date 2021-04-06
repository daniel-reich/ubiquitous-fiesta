
def single_number(nums):
    found = {}
    for i in nums:
        if i in found:
            found[i] += 1
            if found[i] == 3:
                del found[i]
        else:
            found[i] = 1
    return list(found.keys()).pop()

