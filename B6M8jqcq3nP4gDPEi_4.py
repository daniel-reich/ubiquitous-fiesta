
def iso_group(lst, maxi=-float('inf'), index=0, count=0):
    if index == len(lst) - 1:
        return maxi if count == 1 else [maxi] * count
    if lst[index] == maxi:
        count += 1
    if lst[index] > maxi:
        maxi = lst[index]
        count = 1
    return iso_group(lst, maxi, index+1, count)

