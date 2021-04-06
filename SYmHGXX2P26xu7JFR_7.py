
def number_groups(group1, group2, group3):
    nums = []
    for i in group1:
        if i in group2 or i in group3:
            nums.append(i)
    for j in set(group2):
        if j in group1 or j in group3:
            nums.append(j)
    return sorted(set(nums))

