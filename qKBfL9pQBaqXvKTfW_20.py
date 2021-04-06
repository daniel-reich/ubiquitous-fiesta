
def sum_of_slices(lst):
    slices = []
    slices2 = []
    slice_sum = 0
    total_lst = []
    for num in lst:
        slice_sum += num
        if slice_sum < 100:
            slices.append(num)
            if lst.index(num) == len(lst)-1:
                slices2.append(slices)
        elif slice_sum >= 100:
            slices2.append(slices)
            slices = []
            slices.append(num)
            slice_sum = 0
            slice_sum += num
            if lst.index(num) == len(lst)-1:
                slices2.append(slices)
        elif num == 100:
            slices2.append(slices)
            slice_sum = 0
            slices = []
            slices2.append([num])
    for x in slices2:
        total = 0
        for num in x:
            total += num
        total_lst.append(total)
    return total_lst

